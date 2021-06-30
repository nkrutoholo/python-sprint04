import yaml
import mysql.connector

with open('cfg.yaml', 'r') as f:
    config = yaml.full_load(f)
try:
    db = mysql.connector.connect(host=config['settings']['host'],
                                 user=config['settings']['user'],
                                 password=config['settings']['password'])
    print(f"Connected to MySQL server (version {db.get_server_info()}).")
    db.close()
    print("MySQL connection is closed")
except mysql.connector.Error as e:
    print("MySQL connection Error: {}".format(e))
