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
cursor.execute("DROP TABLE IF EXISTS books")
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    cover_image TEXT NOT NULL,
    description TEXT NOT NULL,
    url TEXT NOT NULL,
    html_content TEXT
)
''')

# Create `structure` table for HTML, CSS, JS files
cursor.execute("DROP TABLE IF EXISTS structure")
cursor.execute('''
CREATE TABLE structure (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    file_type TEXT NOT NULL,  -- Now correctly added
    file_content BLOB NOT NULL
)
''')

# Books list (including new books)
books = [
    ("The Tale of Peter Rabbit", "Beatrix Potter", '14838-cover.png', 
     "A children's classic about Peter Rabbit.", "https://online.flipbuilder.com/rias/kedp/",
     insert_file_data('previeux2.html')),
    ("Dog Man", "Dav Pilkey", '51KYLRbfmGL._SY445_SX342_.jpg', 
     "A graphic novel about a dog who is a superhero.", "https://online.flipbuilder.com/fdyv/mtgz/",
     insert_file_data('previeux3.html')),
    ("The One and Only Ivan", "K. A. Applegate", '1.avif',
     "A heartfelt story about a silverback gorilla named Ivan.", "https://online.flipbuilder.com/rias/kedp/",
     insert_file_data('previeux0.html')),
    ("Diary of a Wimpy Kid: The Deep End", "Jeff Kinney", 'download (1).jpg',
     "The latest book in the 'Diary of a Wimpy Kid' series.", "https://online.flipbuilder.com/fdyv/vbpl/",
     insert_file_data('previeux1.html')),
    ("Harold and the Purple Crayon", "Crockett Johnson", 'download (2).jpg',
     "A boy named Harold uses his purple crayon to draw his adventures.", "https://online.fliphtml5.com/zuopu/ymvg/",
     insert_file_data('previeux4.html')),
    ("Holes", "Louis Sachar", 'download (4).jpg',
     "A story about a boy sent to a camp where he digs holes.", "https://online.flipbuilder.com/fdyv/luxv/",
     insert_file_data('previeux5.html')),
    ("Matilda", "Roald Dahl", 'download (5).jpg',
     "The story of a brilliant young girl with special powers.", "https://online.flipbuilder.com/fdyv/joww/",
     insert_file_data('previeux6.html')),
    ("Charlotte's Web", "E.B. White", 'download (6).jpg' ,
     "A story about the friendship between a pig named Wilbur and a spider named Charlotte.",
     "https://online.flipbuilder.com/fdyv/pplb/", insert_file_data('previeux7.html')),
    ("Harry Potter", "J.K. Rowling", 'download (8).jpg' ,
     "The first book in the 'Harry Potter' series about a young wizard.", "https://online.flipbuilder.com/jkdl/trgm/",
     insert_file_data('previeux8.html')),
    ("The Wild Robot", "Peter Brown", 'download (9).jpg' ,
     "A robot learns to survive in the wild after being abandoned on an island.",
     "https://fliphtml5.com/uszmz/rbxc/The-Wild-Robot-By-Peter-Brown-Book/", insert_file_data('previeux9.html')),
    ("Captain Underpants", "Dav Pilkey", 'download (7).jpg' ,
     "The first book in the 'Captain Underpants' series about two kids who create a superhero.",
     "https://online.pubhtml5.com/bbar/tvhn/#p=1", insert_file_data('previeux10.html')),
    ("Stink and the Incredible Shrinking Kid", "Megan McDonald", 'download (10).jpg' ,
     "The story of Stink who shrinks to the size of a doll and faces an adventure.",
     "https://online.flipbuilder.com/xyz123/abc456/", insert_file_data('previeux11.html')),
    ("Dog Man Unleashed", "Dav Pilkey", 'download.jpg' ,
     "The second book in the 'Dog Man' series, filled with more fun and adventure.",
     "https://online.flipbuilder.com/abc123/xyz456/", insert_file_data('previeux12.html')),
    ("Smile", "Ralna Telgemelery", 'download (11).jpg' ,
     "A cute story about a teen girl's tooth tale.", "https://fliphtml5.com/mnnqh/kjda/Smile/",
     insert_file_data('previeux13.html')),
    ("Cheese Colored Camper", "Elisabetta Dami", 'download (12).jpg' ,
     "Story about a mouse named Geronimo Stilton.",
     "https://fliphtml5.com/csoxw/bsmw/Geronimo_Stilton_%3A_A_Cheese_Colored_Camper/",
     insert_file_data('previeux14.html')),
    ("Should I Share My Ice Cream", "Mo Willems", 'download (13).jpg' ,
     "Story about a Elephant who want to share his ice cream with his friend Piggie.",
     "https://online.fliphtml5.com/xjfbd/ihwc/#p=1",
     insert_file_data('previeux15.html')),
    ("Guide to Creative", "Mojang", 'download (14).jpg' ,
     "Book that Guide you in Minecraft Creative Mode",
     "https://fliphtml5.com/xzswt/qajw/",
     insert_file_data('previeux16.html')),
    ("School Bus Trip", "Ellen Philpott", 'download (15).jpg',
     "Story about Peppa Pig and her friends going on a field trip in the mountains",
     "https://pubhtml5.com/krqt/hcwz/Peppa_Pig_-_School_Bus_Trip/",
     insert_file_data('previeux17.html')),
    ("A Pete for Pete", "James Dean", 'download (16).jpg',
     "Story about a cat named Pete getting a goldfish",
     "https://pubhtml5.com/hcsy/xrqg/PETE_THE_CAT_A_Pet_For_Pete/",
     insert_file_data('previeux18.html')),
    ("The Good Egg", "Pete Oswald", 'download (17).jpg',
     "Story about a good and nice egg",
     "https://fliphtml5.com/eairu/cnld/707429470-The-Good-Egg/",
     insert_file_data('previeux19.html')),
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

# Insert HTML, CSS, and JS files into `structure`
structure_files = [
    ('index.html', 'html', insert_file_data('index.html')),
    ('assets/js/offline.html', 'html', insert_file_data('assets/js/offline.html')),
    ('assets/css/styles.css', 'css', insert_file_data('assets/css/styles.css')),
    ('assets/css/swiper-bundle.min.css', 'css', insert_file_data('assets/css/swiper-bundle.min.css')),
    ('assets/js/main.js', 'js', insert_file_data('assets/js/main.js')),
    ('assets/js/script.js', 'js', insert_file_data('assets/js/script.js')),
    ('assets/js/swiper-bundle.min.js', 'js', insert_file_data('assets/js/swiper-bundle.min.js')),
    ('assets/js/scrollreveal.min.js', 'js', insert_file_data('assets/js/scrollreveal.min.js')),
    ('assets/js/suggestions.js', 'js', insert_file_data('assets/js/suggestions.js')),
    ('assets/js/sw.js', 'js', insert_file_data('assets/js/sw.js')),
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
