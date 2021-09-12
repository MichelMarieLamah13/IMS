import mysql.connector

from models.product import Product
from models import *


class ProductRepository:

    @staticmethod
    def find_all():
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "SELECT * FROM products"
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def find_allv2():
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "SELECT pid,name,price,qty,status FROM products"
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def to_value(product, op="add"):
        if op == "add":
            return (product.pid, product.name, product.supplier, product.category, product.price, product.qty,
                    product.status)
        elif op == "update":
            return (product.name, product.supplier, product.category, product.price, product.qty, product.status,
                    product.pid)

    @staticmethod
    def get_product(values):
        return Product(*values)

    @staticmethod
    def add(product):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "INSERT INTO products VALUES(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, ProductRepository.to_value(product))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def update(product):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "UPDATE products " \
              "SET name=%s,supplier=%s,category=%s,price=%s, qty=%s, status=%s" \
              "WHERE pid=%s"
        cursor.execute(sql, ProductRepository.to_value(product, op="update"))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def updatev2(pid, qty, status):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "UPDATE products " \
              "SET qty=%s, status=%s" \
              "WHERE pid=%s"
        cursor.execute(sql, (qty, status, pid))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def delete(pid):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "DELETE FROM products " \
              "WHERE pid=%s"
        cursor.execute(sql, (pid,))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def find(value, key='pid'):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = f"SELECT * FROM products WHERE {key} LIKE '%{value}%'"
        cursor.execute(sql)
        return cursor.fetchall()
