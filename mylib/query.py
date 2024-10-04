"""Query the database"""

import sqlite3


# def query():
#     """Query the database for the top 5 rows of the GroceryDB table"""

#     conn = sqlite3.connect("Murder2015.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM Murder2015")
#     print("Top 5 rows of the Murder2015 table:")
#     print(cursor.fetchall())
#     conn.close()
#     return "Success"


def create_data():
    conn = sqlite3.connect("Murder2015.db")
    cursor = conn.cursor()
    # create execution
    cursor.execute(
        """INSERT INTO Murder2015 (city, state, murders2014, murders2015, change) 
        VALUES('city1', 'NC', '1', '2','1')"""
    )
    cursor.execute("SELECT * FROM Murder2015 WHERE city = 'city1' ")
    print("create: ", cursor.fetchall())
    conn.close()
    return "Create Success"


def read_data():
    conn = sqlite3.connect("Murder2015.db")
    cursor = conn.cursor()
    # read execution
    cursor.execute("SELECT * FROM Murder2015 LIMIT 10")
    print("read 10 from Murder2015")
    conn.close()
    return "Read Success"


def update_data():
    conn = sqlite3.connect("Murder2015.db")
    cursor = conn.cursor()
    # update execution
    cursor.execute(
        """UPDATE Murder2015 
        SET  murders2015 = '3' AND 
        change = '2'  WHERE city= 'city2' """
    )
    print("close")
    conn.commit()
    conn.close()
    return "Update Success"


def delete_data():
    conn = sqlite3.connect("Murder2015.db")
    cursor = conn.cursor()
    # delete execution
    cursor.execute(
        """DELETE FROM Murder2015 
            WHERE city = 'city2'"""
    )
    print("delete")
    conn.commit()
    conn.close()
    return "Delete Success"


# if __name__ == "__main__":
#     create_data()
#     read_data()
#     update_data()
#     delete_data()
