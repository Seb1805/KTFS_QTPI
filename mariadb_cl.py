import mariadb 


def insertData(table,cols,values):
    conn = mariadb.connect(
        user="pyUser",
        password="password",
        host="localhost",
        database="SensorData")
    cur = conn.cursor() 

        
    #insert information 
    try: 
        print(f'INSERT INTO {table} ({cols}) VALUES ({values})')
        cur.execute(f'INSERT INTO {table} ({cols}) VALUES ({values})') 
    except mariadb.Error as e: 
        print(f"Error: {e}")

    conn.commit() 
    print(f"Last Inserted ID: {cur.lastrowid}")
        
    conn.close()