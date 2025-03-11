import os
import yaml
from snowflake.snowpark import Session


print("Code starts from here")
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))

# Get the absolute path of the config.yaml file
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config', 'config.yaml')
print(CONFIG_PATH)

def load_config():
    with open(CONFIG_PATH,'r') as file:
        path_config=yaml.safe_load(file)
    return path_config
config_obj=load_config()
print(config_obj['connection_parameters'])

session =Session.builder.configs(config_obj['connection_parameters']).create()
# print("Hello World")
# df=session.sql('select * from PROD_PERSONAL_DB.ANISH_KUMAR.EMPLOYEES').collect()

# Function to create the table if it doesn’t exist
def create_table():
    session.sql("""
        CREATE TABLE IF NOT EXISTS PROD_PERSONAL_DB.ANISH_KUMAR.URLS (
            short_code STRING PRIMARY KEY,
            long_url STRING NOT NULL,
            clicks INT DEFAULT 0
        )
    """).collect()

# Run table creation at startup
create_table()


def get_session():
    return session

