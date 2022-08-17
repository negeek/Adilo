# WORKFLOW ENGINE

**The Solution  in code.py file implements Triggers, Actions, Conditions as classes**

* Triggers contain actions to be executed if cretain things happen.
* Actions execute when a condition is met.

**From the code.py file below is an Example**

```
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

```
