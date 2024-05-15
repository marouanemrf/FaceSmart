import pypyodbc as adbc

driver_name = 'SQL SERVER'
server_name = 'DESKTOP-B2IG1G0\\SQLEXPRESS'
database_name = 'DB'

conn_str = f"""
     DRIVER={{{driver_name}}};
     SERVER={server_name};
     DATABASE={database_name};
     Trusted_Connection=yes;
"""

connection = adbc.connect(conn_str)

print(connection)