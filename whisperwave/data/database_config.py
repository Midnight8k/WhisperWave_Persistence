import tomllib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database(object):
    """
    Database class for handling SQLAlchemy session and database interactions.

    This class:
    - Loads database configuration from a `config.toml` file.
    - Initializes an SQLAlchemy engine and sessionmaker.
    - Provides methods for adding objects and committing transactions to the database.

    Attributes:
        session (sqlalchemy.orm.Session): SQLAlchemy session used for database operations.
    """

    def __init__(self):
        """
        Initializes the Database object.

        - Reads the database engine URL from the `config.toml` file under the key `database.engine`.
        - Creates an SQLAlchemy engine.
        - Binds a sessionmaker to the engine.
        - Instantiates a session for database operations.
        """
        super(Database, self).__init__()

        with open("config.toml", "rb") as f:
            config = tomllib.load(f)

        engine = create_engine(str(config["database"]["engine"]))

        session_maker = sessionmaker(bind=engine)
        self.session = session_maker()

    def create(self, table):
        """
        Adds a new object (row) to the current session.

        Parameters:
            table (Base): An instance of a SQLAlchemy declarative base class representing a table.
        """
        self.session.add(table)

    def commit(self):
        """
        Commits the current transaction, persisting all staged changes to the database.
        """
        self.session.commit()