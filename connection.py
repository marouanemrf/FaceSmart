import pypyodbc as adbc

driver_name = 'SQL SERVER'
server_name = 'DESKTOP-B2IG1G0\SQLEXPRESS'
data_name = 'DB'

conn_str = f"""
     DRIVER={{{driver_name}}};
     SERVER={server_name};
     DATABASE={data_name};
     Trust_Connection=yes;
"""

connection = adbc.connect(conn_str)

print(f'{connection}')