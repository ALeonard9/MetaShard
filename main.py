#!/usr/bin/python

from functions.database import initialize_db
from functions.database import populate_episode
from functions.database import populate_person
from functions.database import populate_person_episode


import sqlite3

con = sqlite3.connect('database/17s.db')
cur = con.cursor()

# initialize_db(cur)
# populate_episode(cur)
populate_person(cur)
populate_person_episode(cur)

con.commit()

con.close()
