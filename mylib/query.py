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
join_second_query = """
    SELECT *
    FROM default.Murder2015 a
    LEFT JOIN (
        SELECT  
            city,
            state_s,
            try_divide(change, murders2014) AS Murder_Change_Rate
        FROM default.Murder2015
    ) b ON a.city = b.city AND a.state_s = b.state_s
"""

averageMurder_perState_query = """
    SELECT 
        state_s,
        AVG(murders2015) AS average_murders2015_perState
    FROM default.Murder2015
    GROUP BY state_s
"""

SortingMurder_perState_query = """
    SELECT 
        state_s,
        AVG(murders2015) AS average_murders2015_perState
    FROM default.Murder2015
    GROUP BY state_s
    ORDER BY average_murders2015_perState DESC
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
        #create second query
        c.execute(murder_second_query)
        #join
        c.execute(join_second_query)
 
        #aggregation
        c.execute(averageMurder_perState_query)

        #sorting
        c.execute(SortingMurder_perState_query)
        result = c.fetchall()
        print(result)
        c.close()
        return("success")


if __name__ == "__main__":
    query()
