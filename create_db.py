import sqlite3
from faker import Faker
import random
from datetime import datetime
import os

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            province TEXT NOT NULL,
            bio TEXT,
            age INTEGER,
            created_at DATETIME NOT NULL,
            updated_at DATETIME NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Created the people's table.")

def populate_people_table():
    
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    fake = Faker()
    for _ in range(200):
        name = fake.name()
        email = fake.email()
        address = fake.address().replace("\n", ", ")
        city = fake.city()
        province = fake.state()
        bio = fake.text()
        age = random.randint(1, 100)
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        updated_at = created_at
        c.execute('''
            INSERT INTO people (name, email, address, city, province, bio, age, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, email, address, city, province, bio, age, created_at, updated_at))
    conn.commit()
    conn.close()
    print("People table with 200 entries created sucessfully.")

if __name__ == '__main__':
    main()
