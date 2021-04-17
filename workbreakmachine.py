from datetime import datetime
import time
import beepy
# import winsound

import sys

try:
    file_name = sys.argv[1]
except IndexError:
    file_name = 'config.txt'

def read_config(file_name='config.txt'):
    with open(file_name) as f:
        config = dict([line.split(" ", 1) for line in f.read().splitlines()])
    return config

# def to_datetime(hour_minute: str) -> datetime:
def to_datetime(hour_minute):
    # hour, minute = [int(x) for x in hour_minute.split(":")]
    hour, minute = map(int, hour_minute.split(":"))
    t = datetime.now()
    t = t.replace(hour=hour, minute=minute, second=0, microsecond=0)
    return t

def tribe(t, config):
    for k, v in config.items():
        try:
            start, end = map(to_datetime, k.split("-"))
            if start <= t <= end:
                return v
        except ValueError:
            start = to_datetime(k)
            if start <= t:
                return v

BEEPS = {"Praca": 1, "Przerwa": 2, "Przerwa obiadowa": 3}
def main():
    mode = 'Przerwa'
    config = read_config(file_name)

    while True:
        t = datetime.now()
        curr_tribe = tribe(t, config)
        if curr_tribe != mode:
            mode = curr_tribe
            beepy.beep(sound=BEEPS[mode])
            print(mode)
        if curr_tribe == "Koniec":
            break
        time.sleep(1)



main()
