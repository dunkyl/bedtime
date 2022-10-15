# bedtime

Python library for doing something when it's almost time for bed (the computer is going to sleep, or turning off).

```py
import time, bedtime

def do_log():
    f = open("./test.log", "a")
    f.write("i went to sleep\n")
    f.close()

sleeper = bedtime.Listener(on_sleep=do_log)

while True:
    time.sleep(1)

    # later, after lights out...
    # test.log <
    #   i went to sleep
```