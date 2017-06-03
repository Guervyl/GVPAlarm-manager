from alarmDbConnectionManager import AlarmConnectionManager
from AlarmTimeEntity import AlarmTimeEntity

class AlarmTimeDao:
    def __init__(self):
        self.conn = (AlarmConnectionManager()).getConnection
        self.cursor = self.conn.cursor()

    def select(self, where="", limit=0, join="", columnsPlus=""):
        limitStr = ""
        
        if(limit > 0):
            limitStr = "limit " + str(limit)
            
        columnsPlus = ","+columnsPlus if columnsPlus is not "" else columnsPlus
            
        where = " WHERE " + where + " " if where is not "" else where
        
        return self.cursor.execute("SELECT Alarm_times.id as Alarm_timesId, Alarm_times.days as Alarm_timesDays, "
          +"Alarm_times.times as Alarm_timesTimes, Alarm_times.alarm_id as Alarm_timesAlarm_id"
          + columnsPlus
          +" FROM Alarm_times "
          + join+" "
          + where
          + " order by times asc "
          + limitStr).fetchall()
    
    def selectNext(self, day, time=-1, id=-1):
        timeClause = " AND times >= '"+str(time)+"' " if time is not -1 else ""
        whereClause = "(days = '" + str(day)+"'" + str(timeClause) + ") AND Alarm_timesId != '" + str(id)+"'"
        
        join = " JOIN Alarm ON Alarm_times.alarm_id = Alarm.id "
        columnsPlus = "Alarm.id, Alarm.desc"
        
        resultArray = self.select(whereClause, 1, join, columnsPlus)
        
        if(len(resultArray) > 0):
            return AlarmTimeEntity(resultArray[0])
        
        return None

    @property
    def close(self):
        self.conn.close()
        
