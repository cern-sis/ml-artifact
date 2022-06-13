from django.db import connection
from contextlib import closing

def get_slugs(query):
    with closing(connection.cursor()) as cursor: 
        cursor.execute("SELECT slug FROM FTSearch WHERE body MATCH %s", (query,))
        results = cursor.fetchall()
    return results
