# WORKFLOW ENGINE

**The Solution  in code.py file implements Triggers, Actions, Conditions as classes**

* Triggers contain actions to be executed if cretain things happen.
* Actions execute when a condition is met.

**From the code.py file below is an Example**

```
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
**EXPLANATION OF THE CODE ABOVE**
The line  ``` Lists('Dlion').create_list('EmailList') ``` creates a list called EmailList for user Dlion. This is pictured as that the user Dlion is trying to create a Workflow in which has a list(EmailList) which contains a set of suscribers

The line ``` Triggers(user='Dlion').optIn('sussy1', 'EmailList')``` opts in sussy1 to the EmailList

So now we have a list and a suscriber in the list. We need to make things happen. In the code above we want to send Email to suscribers in EmailList but at at a partcular time and also after a set delay. The Email will only be sent even after the time is met and the delay has ended only when the suscriber is on the EmailList.

```sendEmail = Actions().send_email(lst_name='EmailList', msg='Welcome suscriber to my workflow tutorial', user='Dlion',  condition=Conditions('Dlion')) ``` email is composed
                                 
``` delay = Actions().addDelay(dayList=[], timeList=[], next_action=sendEmail, minutes=1) ``` delay of 1 minute is added 


``` process = Triggers(user='Dlion').time(day=17, month=8, year=2022, hour=18, minute=31, timezone='Africa/Lagos', action=delay) ``` Email to be sent on 17/08/2022 at 18:31


```WorkFlow(process).run()``` performs the operations.


