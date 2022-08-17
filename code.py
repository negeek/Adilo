import pytz
import datetime
from datetime import date, timedelta

# variable that acts as a database for list for a user account
global List
List = {}


class Lists:
    def __init__(self, user: str):
        self.user = user

    def create_list(self, lst_name: str):
        try:
            if List[self.user]:
                List[self.user][lst_name] = []
        except:
            List[self.user] = {lst_name: []}


class Triggers:
    def __init__(self, user):
        self.user = user

    def optIn(self, suscriber: str, lst_name: str):
        List[self.user][lst_name].append(suscriber)

    class time:
        def __init__(self, day: int, month: int, year: int, hour: int, minute: int, timezone: str, action):
            self.day = day
            self.month = month
            self.year = year
            self.hour = hour
            self.minute = minute
            self.timezone = timezone
            self.action = action

        def run(self):
            dateTime = datetime.datetime.now(pytz.timezone(self.timezone))
            today = date.today()
            if date(self.year, self.month, self.day) < today or dateTime.hour > self.hour or dateTime.minute > self.minute:
                raise Exception('put today or future date and time')
            while today < date(self.year, self.month, self.day) and dateTime.hour < self.hour and dateTime.minute < self.minute:
                dateTime = datetime.datetime.now(pytz.timezone(self.timezone))
                today = date.today()
            self.action.run()


class Actions:
    class send_email:
        def __init__(self, lst_name: str, msg: str, user: str, condition=None):
            self.lst_name = lst_name
            self.msg = msg
            self.user = user
            self.condition = condition

        def run(self):
            if self.condition:
                for suscriber in List[self.user][self.lst_name]:
                    # sending to each suscriber
                    if self.condition.isOnList(self.lst_name, suscriber):
                        print('To: '+suscriber+'\n'+'Message: '+self.msg)

    class addDelay:
        def __init__(self, dayList: list, timeList: list, next_action, minutes=None):
            '''dayList: It should be in form ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
            timeList(24hr format): It should bein form [startHr, startMin, endHr, endMin]
                                        e.g [12, 0, 13, 0]
            '''
            self.dayList = dayList
            self.timeList = timeList
            self.action = next_action
            self.minutes = minutes

        def run(self):
            if self.dayList == [] and self.minutes and self.timeList == []:
                nowTime = datetime.datetime.now()
                executeTime = nowTime+timedelta(minutes=self.minutes)
                while nowTime < executeTime:
                    nowTime = datetime.datetime.now()
                self.action.run()
            elif self.dayList != [] and self.timeList != [] and not self.minutes:
                dt = datetime.datetime.now()
                if dt.strftime('%A') in self.dayList:
                    while dt.hour < self.timeList[0] or dt.hour > self.timeList[2]:
                        dt = datetime.datetime.now()
                    self.action.run()

    class addRemove:
        def __init__(self, user, lst_name, suscriber, operation):
            self.user = user
            self.lst_name = lst_name
            self.suscriber = suscriber
            self.operation = operation

        def run(self):
            if self.operation == 'add':
                List[self.user][self.lst_name].append(self.suscriber)
                print('Done')
            if self.operation == 'remove':
                List[self.user][self.lst_name].remove(self.suscriber)
                print('Done')
            else:
                print('Invalid action: choose add or remove')


class Conditions:
    def __init__(self, user):
        self.user = user

    def isOnList(self, lst_name, suscriber):
        if suscriber in List[self.user][lst_name]:
            return True
        return False


class WorkFlow:
    def __init__(self, process):
        self.process = process

    def run(self):
        self.process.run()


# EXAMPLE OF A WORKFLOW ENGINE THAT SENDS EMAIL AT A PARTICULAR TIME  BASED ON A CONDITION THAT SUSCRIBER IS IN THE LIST
Lists('Dlion').create_list('EmailList')

Triggers(user='Dlion').optIn('sussy1', 'EmailList')

sendEmail = Actions().send_email(lst_name='EmailList',
                                 msg='Welcome suscriber to my workflow tutorial', user='Dlion',  condition=Conditions('Dlion'))
delay = Actions().addDelay(dayList=[], timeList=[],
                           next_action=sendEmail, minutes=1)

process = Triggers(user='Dlion').time(
    day=17, month=8, year=2022, hour=18, minute=31, timezone='Africa/Lagos', action=delay)

WorkFlow(process).run()
