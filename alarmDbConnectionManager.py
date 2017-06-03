import sqlite3

class AlarmConnectionManager:
    conn = None
    
    def __init__(self):
        #if AlarmConnectionManager.conn is None:
            AlarmConnectionManager.conn = sqlite3.connect("alarm.db")

    @property
    def getConnection(self):
        return AlarmConnectionManager.conn
