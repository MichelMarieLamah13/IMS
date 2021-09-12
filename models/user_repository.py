import mysql.connector

from models.user import User
from models import *


class UserRepository:

    @staticmethod
    def find_all():
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def to_value(user, op="add"):
        if op == "add":
            return (user.uid, user.name, user.utype, user.gender, user.email, user.contact, user.salary, user.address,
                    user.dob, user.doj, user.password)
        elif op == "update":
            return (user.name, user.utype, user.gender, user.email, user.contact, user.salary, user.address,
                    user.dob, user.doj, user.uid)

    @staticmethod
    def get_user(values):
        return User(*values)

    @staticmethod
    def add(user):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, UserRepository.to_value(user))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def update(user):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "UPDATE users " \
              "SET name=%s,utype=%s,gender=%s,email=%s,contact=%s,salary=%s,address=%s,dob=%s,doj=%s" \
              "WHERE uid=%s"
        cursor.execute(sql, UserRepository.to_value(user, op="update"))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def delete(uid):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "DELETE FROM users " \
              "WHERE uid=%s"
        cursor.execute(sql, (uid,))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def find(value, key='uid'):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = f"SELECT * FROM users WHERE {key} LIKE '%{value}%'"
        cursor.execute(sql)
        return cursor.fetchall()
