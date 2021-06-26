# python-attimers
A python timer library that will execute function every desired time

## Example usage
Excute funtion every second minute hour or day

## How to use
Usage code
```
from attimers import *
timer1 = attimers('Interval','days','1:00:00',2)
timer1.start(function)

def function:
  ....
```

  
This example code will execute function every 2 day at 1 am

## Setting time to execute
Ex 15 1:00:00
15 = day
1 = hour
:00 = minute
:00 = second

`attimers('Specific','day','15 1:00:00')`
Execute every 15th at 1 am

`attimers('Interval','hours','00:15:20',1)`
Execute every 1 hour at minute =15 and second = 20
(No need to specific minute in the argument)

`attimers('Interval','minutes','00:00:20',1)`
Execute every 1 minute at second = 20
(No need to specific minute in the argument)

`attimers('Interval','seconds','00:00:00',1)`
Execute every 1 minute at second = 20
(No need to specific time '00:00:00')
