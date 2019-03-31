import database.base
from database.models import tables
from sqlalchemy import exc
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()

class Api(object):
    def __init__(self, bind):
        self._db = None
        self.bind = bind

    def open(self):
        """ creates a session for database transaction if none is active. """
        self._db = Session(bind=self.bind)

    def close(self):
        """ closes the current database session if open. """
        self._db.expunge_all()
        self._db.close()
        self._db = None

    def commit(self):
        return self._db.commit()

    def _clear(self):
        """ clears all tables """
        for table in reversed(database.base.TableBase.metadata.sorted_tables):
            self._db.execute(table.delete())

    def insert(self, obj):
        """ adds a database object to the current session. """
        self._db.add(obj)
    
    def insert_all(self, obj_list):
        """ adds a list of database objects to the current session. """
        self._db.add_all(obj_list)

    def expunge(self, obj):
        """ removes a database object from the current session. """
        self._db.expunge(obj)

    def expunge_all(self, obj_list):
        """ removes a list of database objects from the current session. """
        for item in obj_list:
            self._db.expunge(item)

    def delete(self, obj):
        """ Helper function to encapsulate delete operations.
            Performs automatic commit (see commit()).
            Performs automatic expunge if commit unsuccessful (see expunge()).
            Returns success of operation. """
        self._db.delete(obj)

    def query(self,*args):
        """ universal function for querying the database connection. """
        return self._db.query(*args)
    
    def select(self, table, filter):
        """ helper function for performing simple select operations. """
        return self.query(table).filter(filter)

    def select_all(self, table):
        """ helper function for performing select operations with no filter. """
        return self.query(table).all()
