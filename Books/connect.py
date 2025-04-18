import sqlite3
from flask import Flask, Response

app = Flask(__name__)

# Serve file from DB
def get_file_from_db(filename):
    conn = sqlite3.connect('database/library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT file_content, file_type FROM structure WHERE filename = ?", (filename,))
    result = cursor.fetchone()
    conn.close()

    if result:
        file_content, file_type = result
        if file_type == 'image':
            return Response(file_content, mimetype='image/gif')  # Adjust if jpeg/png
        elif file_type == 'css':
            return Response(file_content, mimetype='text/css')
        elif file_type == 'js':
            return Response(file_content, mimetype='application/javascript')
        elif file_type == 'html':
            return Response(file_content, mimetype='text/html')
    return "File not found", 404

# Homepage
@app.route('/')
def serve_index():
    return get_file_from_db("index.html")

# Book preview
@app.route('/book/<int:book_id>')
def book_details(book_id):
    conn = sqlite3.connect('database/library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT html_content FROM Books WHERE id = ?", (book_id,))
    book = cursor.fetchone()
    conn.close()

    if book:
        return book[0]
    return "Book not found", 404

# Serve assets like CSS, JS, IMG
@app.route('/assets/<path:filename>')
def serve_asset(filename):
    return get_file_from_db(f"assets/{filename}")

# sw.js, offline.html, preview files
@app.route('/<filename>')
def serve_misc(filename):
    if filename == "sw.js":
        return get_file_from_db("assets/js/sw.js")
    elif filename == "offline.html":
        return get_file_from_db("assets/js/offline.html")
    elif filename.startswith("previeux") and filename.endswith(".html"):
        return get_file_from_db(f"assets/js/{filename}")
    return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)
