"""Query the database"""

import os
from databricks import sql
from dotenv import load_dotenv



murder_second_query = """
        WITH murder_change_rate AS(
          SELECT  
              city,
              state_s,
              try_divide(change,murders2014) AS Murder_Change_Rate
          FROM default.Murder2015)

SELECT * FROM murder_change_rate;

        """


def query():
    load_dotenv()
    server_h = os.getenv("sql_server_host")
    access_token = os.getenv("databricks_api_key")
    http_path = os.getenv("sql_http_path")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        c.execute(murder_second_query)
        result = c.fetchall()
        print(result)
        c.close()


# def create_data():
#     conn = sqlite3.connect("Murder2015.db")
#     cursor = conn.cursor()
#     # create execution
#     cursor.execute(
#         """INSERT INTO Murder2015 (city, state, murders2014, murders2015, change)
#         VALUES('city1', 'NC', '1', '2','1')"""
#     )
#     cursor.execute("SELECT * FROM Murder2015 WHERE city = 'city1' ")
#     print("create: ", cursor.fetchall())
#     conn.close()
#     return "Create Success"


# def read_data():
#     conn = sqlite3.connect("Murder2015.db")
#     cursor = conn.cursor()
#     # read execution
#     cursor.execute("SELECT * FROM Murder2015 LIMIT 10")
#     print("read 10 from Murder2015")
#     conn.close()
#     return "Read Success"


# def update_data():
#     conn = sqlite3.connect("Murder2015.db")
#     cursor = conn.cursor()
#     # update execution
#     cursor.execute(
#         """UPDATE Murder2015
#         SET  murders2015 = '3' AND
#         change = '2'  WHERE city= 'city2' """
#     )
#     print("close")
#     conn.commit()
#     conn.close()
#     return "Update Success"


# def delete_data():
#     conn = sqlite3.connect("Murder2015.db")
#     cursor = conn.cursor()
#     # delete execution
#     cursor.execute(
#         """DELETE FROM Murder2015
#             WHERE city = 'city2'"""
#     )
#     print("delete")
#     conn.commit()
#     conn.close()
#     return "Delete Success"


if __name__ == "__main__":
    query()
