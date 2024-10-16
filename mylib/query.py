"""Query the database"""

import os
from databricks import sql
from dotenv import load_dotenv

murder_execute_query="""
WITH murder_change_rate AS(
          SELECT  
              city,
              state_s,
              try_divide(change,murders2014) AS Murder_Change_Rate
          FROM default.Murder2015)

SELECT 
    a.state_s,
    AVG(b.Murder_Change_Rate) AS average_murdersChange_perState
FROM default.Murder2015 a
LEFT JOIN murder_change_rate b ON a.city = b.city AND a.state_s = b.state_s
GROUP BY a.state_s
ORDER BY average_murdersChange_perState DESC;
"""

# murder_second_query = """
#         WITH murder_change_rate AS(
#           SELECT  
#               city,
#               state_s,
#               try_divide(change,murders2014) AS Murder_Change_Rate
#           FROM default.Murder2015)

#             SELECT * FROM murder_change_rate;

#         """

# averageMurder_perState_query = """
#     SELECT 
#         state_s,
#         AVG(murders2015) AS average_murders2015_perState
#     FROM default.Murder2015
#     GROUP BY state_s
# """

# SortingMurder_perState_query = """
#     SELECT 
#         state_s,
#         AVG(murders2015) AS average_murders2015_perState
#     FROM default.Murder2015
#     GROUP BY state_s
#     ORDER BY average_murders2015_perState DESC
# """

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
        #create second query + join + agggregation +sorting
        c.execute(murder_execute_query)
    
        result = c.fetchall()
        print(result)
        c.close()
        return("success")


if __name__ == "__main__":
    query()
