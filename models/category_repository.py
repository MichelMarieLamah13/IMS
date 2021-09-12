import mysql.connector

from models.category import Category
from models import *


class CategoryRepository:

    @staticmethod
    def find_all():
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "SELECT * FROM categories"
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def to_value(category, op="add"):
        if op == "add":
            return (category.cid, category.name)
        elif op == "update":
            return (category.name, category.cid)

    @staticmethod
    def get_category(values):
        return Category(*values)

    @staticmethod
    def add(category):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "INSERT INTO categories VALUES(%s,%s)"
        cursor.execute(sql, CategoryRepository.to_value(category))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def update(category):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "UPDATE categories " \
              "SET name=%s" \
              "WHERE cid=%s"
        cursor.execute(sql, CategoryRepository.to_value(category, op="update"))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def delete(cid):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "DELETE FROM categories " \
              "WHERE cid=%s"
        cursor.execute(sql, (cid,))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def find(value, key='cid'):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = f"SELECT * FROM categories WHERE {key} LIKE '%{value}%'"
        cursor.execute(sql)
        return cursor.fetchall()
