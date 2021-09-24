
import os

# This is a bad place for this import
import pymysql

def get_db_info():
    """
    This is crappy code.

    :return: A dictionary with connect info for MySQL
    """
    db_host = os.environ.get("DBHOST", None)

    if db_host is None:
        db_info = {
            "host": "cloud-force-demo-flask.chny68qeldj2.us-east-1.rds.amazonaws.com",
            "user": "admin",
            "password": "cloudforce1",
            "cursorclass": pymysql.cursors.DictCursor
        }

    else:

        db_info = {
            "host": db_host,
            "user": os.environ.get("DBUSER"),
            "password": os.environ.get("DBPASSWORD"),
            "cursorclass": pymysql.cursors.DictCursor
        }

    return db_info
