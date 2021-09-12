import mysql as mysql

from models import db
import mysql.connector


class ConfigDB:
    @staticmethod
    def create_db():
        """Method to create the database"""
        try:
            if not ConfigDB.db_exists():
                conn = mysql.connector.connect(host=db['host'], user=db['user'], password=db['password'])
                cursor = conn.cursor()
                sql = f"CREATE DATABASE IF NOT EXISTS  {db['database']}"
                cursor.execute(sql)
                conn.commit()
                print(f"Database {db['database']} created successfully")
            else:
                print(f"Database {db['database']} already exists")
        except Exception as err:
            print(f"Error while creating datatbase {db['database']}:{err}")

    @staticmethod
    def db_exists():
        try:
            conn = mysql.connector.connect(host=db['host'], user=db['user'], password=db['password'])
            cursor = conn.cursor()
            sql = "SHOW DATABASES"
            cursor.execute(sql)
            databases = cursor.fetchall()
            for x in databases:
                if db['database'] == x[0]:
                    return True
            return False

        except Exception as err:
            print(f"Error while finding datatbase {db['database']}:{err}")

    @staticmethod
    def drop_db():
        """Method to drop database"""
        try:
            conn = mysql.connector.connect(host=db['host'], user=db['user'], password=db['password'])
            cursor = conn.cursor()
            sql = f"DROP DATABASE  {db['database']}"
            cursor.execute(sql)
            print(f"Database {db['database']} droped successfully")
        except Exception as err:
            print(f"Error while droping datatbase {db['database']}:{err}")
        pass

    @staticmethod
    def create_users_table():
        """Method to create user table"""
        try:
            if not ConfigDB.table_exists(name='users'):
                conn = mysql.connector.connect(**db)
                cursor = conn.cursor()
                sql = """
                CREATE TABLE users(
                    uid int NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    name varchar(255),
                    utype enum('Admin','Employee'),
                    gender enum('Male','Female'),
                    email varchar(255) NOT NULL,
                    contact varchar(255),
                    salary varchar(255),
                    address varchar(255),
                    dob varchar(255),
                    doj varchar(255),
                    password varchar(255) NOT NULL
                )"""
                cursor.execute(sql)
                conn.commit()
                print("Table users created successfully")
            else:
                print("Table users already exists")
        except Exception as err:
            print(f"Error while creating table users:{err}")
        pass

    @staticmethod
    def create_suppliers_table():
        """Method to create suppliers table"""
        try:
            if not ConfigDB.table_exists(name='suppliers'):
                conn = mysql.connector.connect(**db)
                cursor = conn.cursor()
                sql = """
                    CREATE TABLE suppliers(
                        iid int NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        name varchar(255) NOT NULL,
                        contact varchar(255),
                        description varchar(255)
                    )"""
                cursor.execute(sql)
                conn.commit()
                print("Table suppliers created successfully")
            else:
                print("Table suppliers already exists")
        except Exception as err:
            print(f"Error while creating table suppliers:{err}")

    @staticmethod
    def create_categories_table():
        """Method to create categories table"""
        try:
            if not ConfigDB.table_exists(name='categories'):
                conn = mysql.connector.connect(**db)
                cursor = conn.cursor()
                sql = """
                       CREATE TABLE categories(
                           cid int NOT NULL PRIMARY KEY AUTO_INCREMENT,
                           name varchar(255) NOT NULL
                       )"""
                cursor.execute(sql)
                conn.commit()
                print("Table categories created successfully")
            else:
                print("Table categories already exists")
        except Exception as err:
            print(f"Error while creating table categories:{err}")

    @staticmethod
    def create_products_table():
        """Method to create products table"""
        try:
            if not ConfigDB.table_exists(name='products'):
                conn = mysql.connector.connect(**db)
                cursor = conn.cursor()
                sql = """
                           CREATE TABLE products(
                               pid int NOT NULL PRIMARY KEY AUTO_INCREMENT,
                               name varchar(255) NOT NULL,
                               supplier varchar(255),
                               category varchar(255),
                               price varchar(255),
                               qty varchar(255),
                               status enum('Active','Deactive')
                           )"""
                cursor.execute(sql)
                conn.commit()
                print("Table products created successfully")
            else:
                print("Table products already exists")
        except Exception as err:
            print(f"Error while creating table products:{err}")

    @staticmethod
    def table_exists(name):
        try:
            conn = mysql.connector.connect(**db)
            cursor = conn.cursor()
            sql = "SHOW TABLES"
            cursor.execute(sql)
            tables = cursor.fetchall()
            print(tables)
            for x in tables:
                if x[0] == name:
                    return True
            return False

        except Exception as err:
            print(f"Error while finding table {name}:{err}")

    @staticmethod
    def drop_table(name):
        """Method to droping table"""
        try:
            conn = mysql.connector.connect(**db)
            cursor = conn.cursor()
            sql = f"DROP TABLE  {name}"
            cursor.execute(sql)
            print(f"Table {name} successfully dropped from database {db['database']}")
        except Exception as err:
            print(f"Error while droping table {name}:{err}")


if __name__ == "__main__":
    ConfigDB.create_db()
    # users table
    # ConfigDB.drop_table(name='users')
    # ConfigDB.create_suppliers_table()
    # suppliers table
    # ConfigDB.drop_table(name='suppliers')
    # ConfigDB.create_suppliers_table()
    # categories table
    # ConfigDB.drop_table(name='categories')
    # ConfigDB.create_categories_table()
    # categories table
    ConfigDB.drop_table(name='products')
    ConfigDB.create_products_table()
