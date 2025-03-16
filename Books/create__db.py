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

# Create `books` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    cover_image BLOB NOT NULL,
    description TEXT NOT NULL,
    url TEXT NOT NULL,
    html_content TEXT
)
''')

# Create `structure` table for HTML, CSS, JS files
cursor.execute('''
CREATE TABLE IF NOT EXISTS structure (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    file_content TEXT NOT NULL
)
''')

# Books list (including new books)
books = [
    ("The Tale of Peter Rabbit", "Beatrix Potter", insert_file_data('assets/img/14838-cover.png', True),
     "A children's classic about Peter Rabbit.", "https://online.flipbuilder.com/rias/kedp/",
     insert_file_data('previeux2.html')),
    ("Dog Man", "Dav Pilkey", insert_file_data('assets/img/51KYLRbfmGL._SY445_SX342_.jpg', True),
     "A graphic novel about a dog who is a superhero.", "https://online.flipbuilder.com/fdyv/mtgz/",
     insert_file_data('previeux3.html')),
    ("The One and Only Ivan", "K. A. Applegate", insert_file_data('assets/img/1.avif', True),
     "A heartfelt story about a silverback gorilla named Ivan.", "https://online.flipbuilder.com/rias/kedp/",
     insert_file_data('previeux0.html')),
    ("Diary of a Wimpy Kid: The Deep End", "Jeff Kinney", insert_file_data('assets/img/download (1).jpg', True),
     "The latest book in the 'Diary of a Wimpy Kid' series.", "https://online.flipbuilder.com/fdyv/vbpl/",
     insert_file_data('previeux1.html')),
    ("Harold and the Purple Crayon", "Crockett Johnson", insert_file_data('assets/img/download (2).jpg', True),
     "A boy named Harold uses his purple crayon to draw his adventures.", "https://online.fliphtml5.com/zuopu/ymvg/",
     insert_file_data('previeux4.html')),
    ("Holes", "Louis Sachar", insert_file_data('assets/img/download (4).jpg', True),
     "A story about a boy sent to a camp where he digs holes.", "https://online.flipbuilder.com/fdyv/luxv/",
     insert_file_data('previeux5.html')),
    ("Matilda", "Roald Dahl", insert_file_data('assets/img/download (5).jpg', True),
     "The story of a brilliant young girl with special powers.", "https://online.flipbuilder.com/fdyv/joww/",
     insert_file_data('previeux6.html')),
    ("Charlotte's Web", "E.B. White", insert_file_data('assets/img/download (6).jpg', True),
     "A story about the friendship between a pig named Wilbur and a spider named Charlotte.",
     "https://online.flipbuilder.com/fdyv/pplb/", insert_file_data('previeux7.html')),
    ("Harry Potter", "J.K. Rowling", insert_file_data('assets/img/download (8).jpg', True),
     "The first book in the 'Harry Potter' series about a young wizard.", "https://online.flipbuilder.com/jkdl/trgm/",
     insert_file_data('previeux8.html')),
    ("The Wild Robot", "Peter Brown", insert_file_data('assets/img/download (9).jpg', True),
     "A robot learns to survive in the wild after being abandoned on an island.",
     "https://fliphtml5.com/uszmz/rbxc/The-Wild-Robot-By-Peter-Brown-Book/", insert_file_data('previeux9.html')),
    ("Captain Underpants", "Dav Pilkey", insert_file_data('assets/img/download (7).jpg', True),
     "The first book in the 'Captain Underpants' series about two kids who create a superhero.",
     "https://online.pubhtml5.com/bbar/tvhn/#p=1", insert_file_data('previeux10.html')),
    ("Stink and the Incredible Shrinking Kid", "Megan McDonald", insert_file_data('assets/img/download (10).jpg', True),
     "The story of Stink who shrinks to the size of a doll and faces an adventure.",
     "https://online.flipbuilder.com/xyz123/abc456/", insert_file_data('previeux11.html')),
    ("Dog Man Unleashed", "Dav Pilkey", insert_file_data('assets/img/download.jpg', True),
     "The second book in the 'Dog Man' series, filled with more fun and adventure.",
     "https://online.flipbuilder.com/abc123/xyz456/", insert_file_data('previeux12.html')),
    ("Smile", "Ralna Telgemelery", insert_file_data('assets/img/download (11).jpg', True),
     "A cute story about a teen girl's tooth tale.", "https://fliphtml5.com/mnnqh/kjda/Smile/",
     insert_file_data('previeux13.html')),
    ("Cheese Colored Camper", "Elisabetta Dami", insert_file_data('assets/img/download (12).jpg', True),
     "Story about a mouse named Geronimo Stilton.",
     "https://fliphtml5.com/csoxw/bsmw/Geronimo_Stilton_%3A_A_Cheese_Colored_Camper/",
     insert_file_data('previeux14.html')),
    ("Should I Share My Ice Cream", "Mo Willems", insert_file_data('assets/img/download (13).jpg', True),
     "Story about a Elephant who want to share his ice cream with his friend Piggie.",
     "https://online.fliphtml5.com/xjfbd/ihwc/#p=1",
     insert_file_data('previeux15.html')),
    ("Guide to Creative", "Mojang", insert_file_data('assets/img/download (14).jpg', True),
     "Book that Guide you in Minecraft Creative Mode",
     "https://fliphtml5.com/xzswt/qajw/",
     insert_file_data('previeux16.html')),
]

# Insert books
try:
    cursor.executemany('''
    INSERT INTO books (title, author, cover_image, description, url, html_content)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', books)
    print("Books have been successfully inserted into the database.")

except sqlite3.Error as e:
    print(f"Error inserting books: {e}")

# List of HTML, CSS, and JavaScript files
structure_files = [
    ('index.html', insert_file_data('index.html')),
    ('styles.css', insert_file_data('assets/css/styles.css')),
    ('swiper-bundle.min.css', insert_file_data('assets/css/swiper-bundle.min.css')),
    ('main.js', insert_file_data('assets/js/main.js')),
    ('script.js', insert_file_data('assets/js/script.js')),
    ('swiper-bundle.min.js', insert_file_data('assets/js/swiper-bundle.min.js')),
    ('scrollreveal.min.js', insert_file_data('assets/js/scrollreveal.min.js')),
    ('suggestions.js', insert_file_data('assets/js/suggestions.js'))
]

# Insert structure files
try:
    cursor.executemany('''
    INSERT INTO structure (filename, file_content)
    VALUES (?, ?)
    ''', structure_files)
    print("HTML, CSS, and JavaScript files have been successfully inserted into the database.")

except sqlite3.Error as e:
    print(f"Error inserting structure files: {e}")

# Commit and close connection
conn.commit()
conn.close()
