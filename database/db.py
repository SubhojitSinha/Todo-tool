import sqlite3
import os
# from dotenv import load_dotenv # pip install python-dotenv

class sqliteDB:
    __conn  = ''
    __table = 'test_table'
    __db    = 'todo.db'
    def __init__(self) -> None:
        # load_dotenv()
        # self.__db    = os.path.join("database", os.getenv('DB_NAME'))
        # self.__table = os.getenv('SCRAP_TABLE')
        self.__db    = os.path.join("database", 'todo.db')
        self.__conn  = sqlite3.connect(self.__db)

    def table_exist(self):
        listOfTables = self.__conn.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.__table}'; ").fetchall()
        return True if not listOfTables == [] else False

    def create_table(self) -> None:
        try:
            query = '''CREATE TABLE {0}(
                id         INTEGER      PRIMARY KEY AUTOINCREMENT,
                test_col1  VARCHAR(255) NOT     NULL,
                created_at TEXT         DEFAULT CURRENT_TIMESTAMP NOT NULL
            );'''
            if not self.table_exist():
                print(self.__db)
                print(self.__conn)

                self.__conn.execute(query.format(self.__table))
                print ("Table created successfully");
            else:
                print('Table already exists. Skipping table creation')
        except Exception as e:
            print("Got some exception", e)

    def execute_query(self, query, is_fetch = None):
        try:
            cursor=self.__conn.cursor()
            cursor.execute(query)
            self.__conn.commit()
            # return cursor.lastrowid if 'INSERT' in query else True
            return cursor.lastrowid if 'INSERT' in query else cursor.fetchall()
        except Exception as e:
            # Handle any type of exception
            print("An error occurred:", str(e),query)

    def generate_insert_query(self, table_name, data_dict):
        keys         = ', '.join(data_dict.keys())
        values       = ', '.join([f"'{value}'" for value in data_dict.values()])

        insert_query = f"INSERT INTO {table_name} ({keys}) VALUES ({values})"
        return insert_query

    def generate_update_query(self, table_name, data_dict, id_key, id_value):
        query_set = set()
        for key,value in data_dict.items():
            query_set.add( f"'{key}' = '{value}' ")

        set_query    = ''.join(query_set) if len(query_set) == 1 else ', '.join(query_set)
        update_query = f"UPDATE {table_name} SET {set_query} WHERE {id_key} = '{id_value}'"
        return update_query

    def generate_delete_query(self, table_name, id_key, id_value):
        update_query = f"DELETE FROM {table_name} WHERE {id_key} = '{id_value}'"
        return update_query

    def insert_data(self, data_dict: dict):
        query = self.generate_insert_query(self.__table, data_dict)
        print(query)
        return self.execute_query(query)

    def delete_data(self, id_key, id_value):
        query = self.generate_delete_query(self.__table,id_key, id_value)
        return self.execute_query(query)

    def update_data(self, data_dict, id_key, id_value):
        query = self.generate_update_query(self.__table, data_dict, id_key, id_value)
        return self.execute_query(query)

    def column_search(self, table_name, column_name, search_term):
        query       = f"SELECT * FROM {table_name} WHERE {column_name} LIKE ?"
        search_term = f'%{search_term}%'
        cursor      = self.__conn.cursor()

        cursor.execute(query, (search_term,))
        return cursor.fetchall()

    def get_all_unsynced_rows(self):
        self.__conn.row_factory = sqlite3.Row
        query = f"SELECT * FROM {self.__table} WHERE is_synced = '0'"
        cursor= self.__conn.cursor()

        cursor.execute(query)
        return [dict(row) for row in cursor.fetchall()]

    def get_all_unsynced_artwork_rows(self):
        self.__conn.row_factory = sqlite3.Row
        query = f"SELECT * FROM {self.__table} WHERE artwork_collected = '0'"
        cursor= self.__conn.cursor()

        cursor.execute(query)
        return [dict(row) for row in cursor.fetchall()]

    def get_base_db_dict(self)->dict:
        data_dict = dict()
        data_dict = {
            # 'id'             : 0, # Autoincrement column
            'test_col1'        : '',
            'created_at'       : '',
        }
        return data_dict

    def get_row_by_test_col1(self, test_col1):
        query =f"SELECT * FROM {self.__table} WHERE test_col1='{test_col1}';"

        try:
            cursor=self.__conn.cursor()
            return cursor.execute(query).fetchall()
            # self.__conn.commit()
            # return cursor.lastrowid if 'INSERT' in query else True
        except Exception as e:
            # Handle any type of exception
            print("An error occurred:", str(e), query)

# new = sqliteDB()
# new.create_table()
# data_dict = {
#     'test_col1'     : 'Test Col Test Data',
#     'created_at'    : '2024-02-04 10:11:12',
# }
# print(new.insert_data(data_dict))
# raise RuntimeError("test 1")
# print(new.delete_data('id','3'))
# print(new.update_data({'test_col1':'UPDATED'},'id','1'))
# print(new.update_data({'test_col1':'UPDATED AGAIN','created_at': 'altered'},'id','1'))
# new = sqliteDB()
# print(new.column_search(new.table, 'created_at', '1'))