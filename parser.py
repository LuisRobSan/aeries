from bs4 import BeautifulSoup
from sqlite3 import connect
import re

def parse_gradebook(source, c):
    parsed_gradebook = dict()
    name, grade = (0, 4)
    soup = BeautifulSoup(source, "html.parser")
    rows = soup.find_all("tr", {"class":"k-alt"})

    for row in rows:
        siblings = row.td.find_next_siblings()
        data = [(siblings[0].get_text(), siblings[4].get_text())]
        c.executemany("INSERT INTO grades VALUES (?, ?)", data)
        if row.next_sibling != None:
            siblings_even = row.next_sibling.td.find_next_siblings()
            data = [(
                siblings_even[0].get_text(),
                siblings_even[4].get_text()
            )]
            c.executemany("INSERT INTO grades VALUES (?, ?)", data)

if __name__ == "__main__":
    with open("source.txt", "r") as f:
        source = f.read()
        conn = connect("grades.db")
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS grades")
        c.execute("CREATE TABLE grades (course text, grade real)")
        parse_gradebook(source, c)
        conn.commit()
        conn.close()
