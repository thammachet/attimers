# python-attimers
A python timer library that will execute function every desired time

## Features
Excute funtion every second minute hour or day

## Requirements
```
pip install DateTime
pip install python-dateutil
```

## How to use
1. Clone attimers.py
2. Put it with python file you wish to use
3. Add the example following code in to the python file.
```
from attimers import *
timer1 = attimers('Interval','days','1:00:00',2)
timer1.start(function)

def function:
  ....
```

  
This example code will execute function every 2 day at 1 am

## Setting time to execute
Example 

```
attimers('Specific','day','15 1:00:00')
```
15 1:00:00
15 = day
1 = hour
:00 = minute
:00 = second
Will execute every 15th at 1 am

```
attimers('Interval','hours','00:15:20',1)
```
Execute every 1 hour at minute =15 and second = 20
(No need to specific hour in the argument)

```
attimers('Interval','hours','00:45:50',4)
```
Execute every 4 hour at minute =45 and second = 50
(No need to specific hour in the argument)

```
attimers('Interval','minutes','00:00:20',1)
```
Execute every 1 minute at second = 20
(No need to specific minute in the argument)

```
attimers('Interval','seconds','00:00:00',1)
```
Execute every 1 minute at second = 20
(No need to specific time purt '00:00:00')
