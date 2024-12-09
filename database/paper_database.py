#paper_database.py
import sqlite3
import numpy as np

class PaperDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('papers.db')
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        """Create the necessary tables for storing papers."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS papers (
                                id INTEGER PRIMARY KEY,
                                title TEXT,
                                abstract TEXT,
                                authors TEXT,
                                journal TEXT,
                                publication_date TEXT,
                                embedding BLOB)''')
        self.conn.commit()

    def store_paper(self, title, abstract, details, embedding):
        """Store the paper data and its embedding in the database."""
        authors = ", ".join(details["authors"])
        journal = details["journal"]
        publication_date = details["publication_date"]
        
        # Convert embedding (numpy array) to binary
        embedding_blob = sqlite3.Binary(np.array(embedding).tobytes())
        
        self.cursor.execute('''INSERT INTO papers (title, abstract, authors, journal, publication_date, embedding)
                               VALUES (?, ?, ?, ?, ?, ?)''',
                            (title, abstract, authors, journal, publication_date, embedding_blob))
        self.conn.commit()

    def search_paper_by_title(self, title):
        """Search for a paper in the database by its title."""
        self.cursor.execute('''SELECT * FROM papers WHERE title LIKE ? LIMIT 1''', ('%' + title + '%',))
        return self.cursor.fetchone()

    def paper_exists(self, title):
        """Check if a paper with the given title exists in the database."""
        self.cursor.execute("SELECT id FROM papers WHERE title = ?", (title,))
        return self.cursor.fetchone() is not None

    def close(self):
        """Close the database connection."""
        self.conn.close()
