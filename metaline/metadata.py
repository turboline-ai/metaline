from sqlalchemy import create_engine, inspect
from sqlalchemy.exc import SQLAlchemyError

def get_metadata(connection_string: str, table_name: str):
    try:
        engine = create_engine(connection_string)
        inspector = inspect(engine)
        
        if table_name not in inspector.get_table_names():
            raise ValueError(f"Table {table_name} does not exist in the database.")
        
        columns_info = inspector.get_columns(table_name)
        metadata = [
            {
                "name": col["name"],
                "type": str(col["type"]),
                "nullable": col["nullable"],
                "default": col.get("default"),
            }
            for col in columns_info
        ]
        return metadata
    except SQLAlchemyError as e:
        print(f"Error: {e}")
        return None
    finally:
        engine.dispose()