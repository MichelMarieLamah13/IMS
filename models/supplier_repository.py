import mysql.connector

from models.supplier import Supplier
from models import *


class SupplierRepository:

    @staticmethod
    def find_all():
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "SELECT * FROM suppliers"
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def to_value(supplier, op="add"):
        if op == "add":
            return (supplier.iid, supplier.name, supplier.contact, supplier.description)
        elif op == "update":
            return (supplier.name, supplier.contact, supplier.description, supplier.iid)

    @staticmethod
    def get_supplier(values):
        return Supplier(*values)

    @staticmethod
    def add(supplier):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "INSERT INTO suppliers VALUES(%s,%s,%s,%s)"
        cursor.execute(sql, SupplierRepository.to_value(supplier))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def update(supplier):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "UPDATE suppliers " \
              "SET name=%s,contact=%s,description=%s" \
              "WHERE iid=%s"
        cursor.execute(sql, SupplierRepository.to_value(supplier, op="update"))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def delete(iid):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = "DELETE FROM suppliers " \
              "WHERE iid=%s"
        cursor.execute(sql, (iid,))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def find(value, key='iid'):
        conn = mysql.connector.connect(**db)
        cursor = conn.cursor()
        sql = f"SELECT * FROM suppliers WHERE {key} LIKE '%{value}%'"
        cursor.execute(sql)
        return cursor.fetchall()
