from flask import g, request
import pymysql
import config


def openDbconnection():
    try:
        connection = pymysql.connect(
            host=config.MYSQL_HOST, user=config.MYSQL_USER, passwd=config.MYSQL_PASSWORD, db=config.MYSQL_DB)
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        return connection, cursor
    except Exception as e:
        print(e)
        return False


def closeDbconnection(connection):
    return connection.close()


def get_db_connection():
    if 'connection' not in g or 'cursor' not in g:
        g.connection, g.cursor = openDbconnection()
    return g.connection, g.cursor


def destroy_db_connection():
    connection = g.pop("connection", None)
    cursor = g.pop("cursor", None)
    if connection is not None:
        if connection.open:
            connection.close()
