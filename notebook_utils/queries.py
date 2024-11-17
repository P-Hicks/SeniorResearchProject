
import psycopg2

# from asgiref.sync import sync_to_async

# @sync_to_async
def run_query(query, fetch=True):
    result = None
    try:
        # connection = psycopg2.connect("dbname=data_with_time user=root password=root")
        # Connect to DB and create a cursor
        # sqlite_connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        cursor.execute(query) 
        # Fetch and output result
        if fetch:
            result = cursor.fetchall()
        else:
            connection.commit()
        # Close the cursor
        cursor.close()
        
    # Handle errors
    # except sqlite3.Error as error:
        # print('Error occurred - ', error)
 
    # Close DB Connection irrespective of success
    # or failure
    finally:
        if connection:
            connection.close()
    return result

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return None
    # except IOError as e:
    #     return None
    

def run_query_file(path, fetch=True):
    query = read_file(path)
    return run_query(query, fetch=fetch)