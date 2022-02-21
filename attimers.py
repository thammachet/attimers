from datetime import timedelta,datetime
from dateutil.relativedelta import *

import threading
class attimers():
    def __init__(self,mode,mode1,v1 = None,v2 = None,fe=True):
        self.mode = mode
        self.mode1 = mode1
        self.v1=v1
        self.v2=v2
        self.fe=fe

    def start(self,func):
        now=datetime.today()
        if self.mode == "Interval":
            if self.v1 != None:
                self.dt=datetime.strptime(self.v1,'%H:%M:%S').time()
            if self.mode1 == 'days':
                nxt=now.replace(day=now.day,hour=self.dt.hour,minute=self.dt.minute,second=self.dt.second)+timedelta(days=self.v2)
            if self.mode1 == 'hours':
                nxt=now.replace(day=now.day,hour=now.hour,minute=self.dt.minute,second=self.dt.second)+timedelta(hours=self.v2)
            if self.mode1 == 'minutes':
                nxt=now.replace(day=now.day,hour=now.hour,minute=now.minute,second=self.dt.second)+timedelta(minutes=self.v2)
            if self.mode1 == 'seconds':
                nxt=now.replace(day=now.day,hour=now.hour,minute=now.minute,second=now.second)+timedelta(seconds=self.v2)
        if self.mode == "Specific":
            if self.mode1 == 'day':
                self.dt=datetime.strptime(self.v1,"%d %H:%M:%S")
                self.dt=self.dt.replace(year=now.year,month=now.month)
                # Next date is already passed.
                if self.dt.day < now.day:
                    nxt=now.replace(year=now.year,month=now.month,day=self.dt.day,hour=self.dt.hour,minute=self.dt.minute,second=self.dt.second)+relativedelta(months=+1)
                else:
                    nxt=now.replace(day=self.dt.day,hour=self.dt.hour,minute=self.dt.minute,second=self.dt.second)
        dt=nxt-now
        self.secs=dt.total_seconds()
        if self.fe == True:
            func()
        else :
            self.fe = True
        print("Next scheduler : "+str(nxt))
        print("Second left : "+str(self.secs))
        t = threading.Timer(self.secs, self.start,[func])
        t.daemon=True
        t.start()
