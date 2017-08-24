import psycopg2

CONNECTION_STR = "dbname='bans' user='bans' host='localhost' password='pass'"


def query(sql_str, connection_str=CONNECTION_STR):
    try:
        with psycopg2.connect(connection_str) as connection:
            with connection.cursor() as cursor:
                if sql_str.startswith("SELECT"):
                    cursor.execute(sql_str)
                    return cursor.fetchall()
                else:
                    cursor.execute(sql_str)
                    connection.commit()
                    return sql_str.split()[0] + " done."
    except psycopg2.DatabaseError as exception:
        print(exception)
