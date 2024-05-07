from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import threading

class AtTimers():
    def __init__(self, schedule_type, interval_unit, start_time=None, interval_value=None, first_execution=True):
        self.schedule_type = schedule_type
        self.interval_unit = interval_unit
        self.start_time = start_time
        self.interval_value = interval_value
        self.first_execution = first_execution

    def start(self, callback_function):
        current_time = datetime.today()
        if self.schedule_type == "Interval":
            if self.start_time is not None:
                self.scheduled_time = datetime.strptime(self.start_time,'%H:%M:%S').time()
            if self.interval_unit == 'days':
                next_execution = current_time.replace(hour=self.scheduled_time.hour, minute=self.scheduled_time.minute, second=self.scheduled_time.second)
            elif self.interval_unit == 'hours':
                next_execution = current_time.replace(hour=current_time.hour, minute=self.scheduled_time.minute, second=self.scheduled_time.second)
            elif self.interval_unit == 'minutes':
                next_execution = current_time.replace(hour=current_time.hour, minute=current_time.minute, second=self.scheduled_time.second)
            elif self.interval_unit == 'seconds':
                next_execution = current_time.replace(hour=current_time.hour, minute=current_time.minute, second=current_time.second)
            while next_execution <= current_time:
                if self.interval_unit == 'days':
                    next_execution = next_execution + timedelta(days=self.interval_value)
                elif self.interval_unit == 'hours':
                    next_execution = next_execution + timedelta(hours=self.interval_value)
                elif self.interval_unit == 'minutes':
                    next_execution = next_execution + timedelta(minutes=self.interval_value)
                elif self.interval_unit == 'seconds':
                    next_execution = next_execution + timedelta(seconds=self.interval_value)
        elif self.schedule_type == "Specific":
            if self.interval_unit == 'day':
                self.scheduled_date_time = datetime.strptime(self.start_time,"%d %H:%M:%S")
                self.scheduled_date_time = self.scheduled_date_time.replace(year=current_time.year, month=current_time.month)
                # If the next date is already passed.
                if self.scheduled_date_time.day <= current_time.day:
                    next_execution = current_time.replace(year=current_time.year, month=current_time.month, day=self.scheduled_date_time.day, hour=self.scheduled_date_time.hour, minute=self.scheduled_date_time.minute, second=self.scheduled_date_time.second) + relativedelta(months=+1)
                else:
                    next_execution = current_time.replace(day=self.scheduled_date_time.day, hour=self.scheduled_date_time.hour, minute=self.scheduled_date_time.minute, second=self.scheduled_date_time.second)
        time_until_next_execution = next_execution - current_time
        seconds_until_next_execution = time_until_next_execution.total_seconds()
        if self.first_execution:
            callback_function()
        else:
            self.first_execution = True
        print("Next scheduler: " + str(next_execution))
        print("Seconds left: " + str(seconds_until_next_execution))
        timer = threading.Timer(seconds_until_next_execution, self.start, [callback_function])
        timer.daemon = True
        timer.start()