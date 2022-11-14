import pyodbc

def create_connection():
    conn = None
    try:
        conn = pyodbc.connect("driver={SQL Server};"
                        "server=DESKTOP-H9LPT8Q;"
                        "database=Definite CA2;"
                        "trusted_connection=yes;")
    except pyodbc.Error as e:
        print(f"The error '{e}' occurred")
    return conn

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except pyodbc.Error as e:
        print(f"The error '{e}' occurred")

def execute_query_commit(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        
    except pyodbc.Error as e:
        print(f"The error '{e}' occurred")