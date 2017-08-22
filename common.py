import psycopg2

CONNECTION_STR = "dbname='bans' user='bans' host='localhost' password='pass'"


def query(query_str, connection_str=CONNECTION_STR):
    try:
        with psycopg2.connect(connection_str) as connection:
            with connection.cursor() as cursor:
                if query_str.startswith("SELECT"):
                    cursor.execute(query_str)
                    return cursor.fetchall()
                else:
                    cursor.execute(query_str)
                    connection.commit()
                    return query_str.split()[0] + " done."
    except psycopg2.DatabaseError as exception:
        print(exception)
