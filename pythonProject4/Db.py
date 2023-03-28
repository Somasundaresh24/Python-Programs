import sqlite3
from sqlite3 import Error
def create_connection():
  """ create a database connection to a database that resides in the memory
  """
  try:
    conn = sqlite3.connect(':memory:')
    print("SQLite Version:",sqlite3.version)
  except Error as e:
    print(e)
  finally:
    conn.close()
create_connection()

import sqlite3
from sqlite3 import Error
def create_connection():
  """ create a database connection to a database that resides in the memory
  """
  try:
    conn = sqlite3.connect(':memory:')
    print("SQLite Version:",sqlite3.version)
  except Error as e:
    print(e)
  finally:
    conn.close()
create_connection()
# Asghar Pasha7:54 PM
# CREATE TABLE languages (
#    language_id INTEGER,
#    name TEXT NOT NULL,
#    PRIMARY KEY (language_id)
# )
# CREATE TABLE languages (
#    language_id INTEGER,
#    name TEXT NOT NULL,
#    PRIMARY KEY (language_id)
# )
# Asghar Pasha7:57 PM
#
#
