import sqlite3
from flask import Flask, Response

app = Flask(__name__)

# Function to fetch file content from the database
def get_file_from_db(filename):
    conn = sqlite3.connect('database/library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT file_content, file_type FROM structure WHERE filename = ?", (filename,))
    result = cursor.fetchone()
    conn.close()

    if result:
        file_content, file_type = result
        if file_type == 'image':
            return Response(file_content, mimetype='image/jpeg')
        elif file_type == 'css':
            return Response(file_content, mimetype='text/css')
        elif file_type == 'js':
            return Response(file_content, mimetype='application/javascript')
        elif file_type == 'html':
            return Response(file_content, mimetype='text/html')
    return "File not found", 404

# Route for index.html (loaded from database)
@app.route('/')
def serve_index():
    return get_file_from_db("index.html")

# Route to display book details + Preview button
@app.route('/book/<int:book_id>')
def book_details(book_id):
    conn = sqlite3.connect('database/library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, cover_image, description, url, html_content FROM Books WHERE id = ?", (book_id,))
    book = cursor.fetchone()
    conn.close()

    if book:
        title, author, image, description, url, html_content = book

        html = f"""
        <html>
            <head>
                <title>{title}</title>
                <link rel="stylesheet" href="/assets/style.css">
            </head>
            <body>
                <h1>{title}</h1>
                <p><strong>Author:</strong> {author}</p>
                <img src="/assets/img/{image}" alt="{title}" style="width:200px;height:auto;"><br>
                <p>{description}</p>
                <a href="{url}" target="_blank">Read More</a><br>
                <p>{html_content}</p>
                <br><a href="/">Back to library</a>
            </body>
        </html>
        """
        return html
    return "Book not found", 404

# Route to serve preview files directly (no folder)
@app.route('/<filename>')
def serve_preview(filename):
    if filename.startswith("previeux") and filename.endswith(".html"):
        # Extra security: Prevent path traversal attacks
        if '..' not in filename and '/' not in filename:
            return get_file_from_db(filename)
    return "File not found", 404

# Serve assets (CSS, JS, images)
@app.route('/assets/<path:filename>')
def serve_asset(filename):
    return get_file_from_db(f"assets/{filename}")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
