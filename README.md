# Adilo

**The Solution  in code.py file implements Triggers, Actions, Conditions as classes**

* Triggers contain actions to be executed if cretain things happen.
* Actions execute when a condition is met.

**From the code.py file below is an Example**

```
# EXAMPLE OF A WORKFLOW ENGINE THAT SENDS EMAIL AT A PARTICULAR TIME AND WAITS FOR 2 MINUTEs BEFORE SENDING

Triggers(user='Dlion').optIn('sussy1', 'EmailList')

sendEmail = Actions().send_email(lst_name='EmailList',
                                 msg='Welcome suscriber to my workflow tutorial', user='Dlion', condition=Conditions())

delay = Actions().addDelay(dayList=[], timeList=[],
                           next_action=sendEmail, minutes=2)

Triggers(user='Dlion').time(
    day=17, month=8, year=2022, hour=18, minute=30, action=delay)

```
