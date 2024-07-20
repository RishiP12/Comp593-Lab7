import sqlite3
import pandas as pd
import os

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')
csv_path = os.path.join(script_dir, 'old_people.csv')

def main():
    old_people = query_old_people()
    print_old_people(old_people)
    save_to_csv(old_people)

def query_old_people():
    """Queries the people table for all people who are at least 50 years old"""
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        SELECT name, age FROM people
        WHERE age >= 50
    ''')
    old_people = c.fetchall()
    conn.close()
    return old_people

def print_old_people(old_people):
    """Prints the names and ages of all old people"""
    for person in old_people:
        print(f'{person[0]} is {person[1]} years old.')

def save_to_csv(old_people):
    """Saves the names and ages of all old people to a CSV file"""
    df = pd.DataFrame(old_people, columns=['Name', 'Age'])
    df.to_csv(csv_path, index=False)

if __name__ == '__main__':
    main()
