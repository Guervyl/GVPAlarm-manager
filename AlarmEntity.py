class AlarmEntity:
    def __init__(self, alarmDao):
        self.id = alarmDao[0]
        self.description = alarmDao[1]
        self.times = []
        
    def __str__(self):
        return "AlarmEntity:: id: "+str(self.id)+"; description: "+str(self.description)