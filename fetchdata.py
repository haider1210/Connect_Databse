import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class OracleDatabase:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)

    def execute_query(self, query):
        try:
            with Session(bind=self.engine) as session:
                result = session.execute(query)
                df = pd.DataFrame(result)
            return df

        except Exception as e:
            return f"An error occurred: {e}"
        
    def execute_queryVTL(self, query):
        try:
            with Session(bind=self.engine) as session:
                result = session.execute(query)
                pd.set_option('display.max_colwidth', 10000)
                df = pd.DataFrame(result)
                data = (df['command_template'].iloc[0])
            return f'''{data}'''

        except Exception as e:
            return f"An error occurred: {e}"

        
    



   

