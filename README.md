
# python-attimers

A Python timer library that executes functions at specified intervals or specific times, based on detailed scheduling options.

## Features
- Execute functions at specific times or at regular intervals (days, hours, minutes, seconds).

## Requirements
This library requires the installation of additional Python packages:
```bash
pip install DateTime
pip install python-dateutil
```

## Installation
1. Clone the repository and include `attimers.py` in your project directory.

## Usage
Here's a basic example to get you started:

```python
from attimers import AtTimers

# Define your function to be scheduled
def my_scheduled_function():
    print("Function executed!")

# Set up the timer to execute the function every 2 days at 1:00 AM
timer = AtTimers('Interval', 'days', '1:00:00', 2)
timer.start(my_scheduled_function)
```

This example sets up a timer to execute `my_scheduled_function` every 2 days at 1 AM.

## Setting Time to Execute
### Specific Time Execution
Execute a function at a specific time on a given day each month:
```python
AtTimers('Specific', 'day', '15 1:00:00')
```
This schedules the function to execute every 15th of the month at 1 AM.

### Interval Execution
Here are examples of setting intervals at various units of time:
```python
# Every hour at 15 minutes and 20 seconds
AtTimers('Interval', 'hours', '00:15:20', 1)

# Every 4 hours at 45 minutes and 50 seconds
AtTimers('Interval', 'hours', '00:45:50', 4)

# Every minute at 20 seconds
AtTimers('Interval', 'minutes', '00:00:20', 1)

# Every second
AtTimers('Interval', 'seconds', '00:00:00', 1)
```

Note: When setting intervals, specify only the units of time relevant to the interval.
