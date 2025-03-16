import sqlite3
import os


# Function to read file data (text for HTML/CSS/JS, binary for images)
def insert_file_data(file_path, is_binary=False):
    full_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', file_path))

    if os.path.exists(full_path):
        with open(full_path, 'rb' if is_binary else 'r', encoding=None if is_binary else 'utf-8') as file:
            return file.read()
    else:
        print(f"Error: {full_path} not found.")
        return None


# Connect to SQLite database
conn = sqlite3.connect('database/library.db')
cursor = conn.cursor()

# Drop and recreate `structure` table to fix column issue
cursor.execute("DROP TABLE IF EXISTS structure")
cursor.execute('''
CREATE TABLE structure (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    file_type TEXT NOT NULL,  -- Now correctly added
    file_content BLOB NOT NULL
)
''')

# Insert HTML, CSS, and JS files into `structure`
structure_files = [
    ('index.html', 'html', insert_file_data('index.html')),
    ('assets/css/styles.css', 'css', insert_file_data('assets/css/styles.css')),
    ('assets/css/swiper-bundle.min.css', 'css', insert_file_data('assets/css/swiper-bundle.min.css')),
    ('assets/js/main.js', 'js', insert_file_data('assets/js/main.js')),
    ('assets/js/script.js', 'js', insert_file_data('assets/js/script.js')),
    ('assets/js/swiper-bundle.min.js', 'js', insert_file_data('assets/js/swiper-bundle.min.js')),
    ('assets/js/scrollreveal.min.js', 'js', insert_file_data('assets/js/scrollreveal.min.js')),
    ('assets/js/suggestions.js', 'js', insert_file_data('assets/js/suggestions.js'))
]

# Insert images into `structure`
image_folder = 'assets/img/'
for filename in os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', image_folder))):
    file_path = os.path.join(image_folder, filename)
    structure_files.append((file_path, 'image', insert_file_data(file_path, True)))

# Insert files into `structure` table
for file in structure_files:
    if file[2]:  # Ensure file content is not None
        cursor.execute('''
            INSERT INTO structure (filename, file_type, file_content)
            VALUES (?, ?, ?)
        ''', file)

# Commit and close connection
conn.commit()
conn.close()
print("Database updated successfully with all HTML, CSS, JS, and images in the structure table!")
