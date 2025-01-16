import pymysql

def test_connection():
    connection = pymysql.connect(
        host='localhost',
        user='my_user',
        password='Hello123',
        db='website_database'
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            print("Connected to MySQL version:", version[0])
    finally:
        connection.close()

if __name__ == "__main__":
    test_connection()
