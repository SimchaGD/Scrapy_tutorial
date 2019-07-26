import sqlite3

# Maak verbinding met database
# Als de db nog niet bestaat, dan wordt die aangemaakt
conn = sqlite3.connect("myquotes.db")
curr = conn.cursor()

# Run this section ones!

# Maak de tabel aan met de cursor
# definieer de tabel namen en de soort datatype
curr.execute("""
CREATE TABLE quotes_tb(
title text,
author text,
tag text
)
""")

# Voeg wat waarde toe aan de tabel
curr.execute("""
INSERT INTO quotes_tb VALUES ("Python is awesome!", "BuildWithPython", "Python")
             """)

# Commit alle veranderingen en sluit de verbinding met de database
conn.commit()
conn.close()