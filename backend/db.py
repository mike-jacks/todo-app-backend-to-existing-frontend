from sqlmodel import Field, SQLModel, create_engine
from models import Todo

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///data/{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def main():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    main()

