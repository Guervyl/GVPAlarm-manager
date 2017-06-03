from alarmDbConnectionManager import AlarmConnectionManager

class AlarmEntity:
    def __init__(self):
        self.conn = (AlarmConnectionManager()).getConnection
        self.cursor = self.conn.cursor()
        self.times = None

    @property
    def select(self):
        return self.cursor.execute("SELECT * FROM Alarm").fetchall()

    @property
    def close(self):
        self.conn.close()
