import random
from random import randrange, randint
import datetime 
from time import sleep
# Format: ip.ip.ip.ip - HH:MM:SS - HH:MM:SS

bad_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

# print(bad_ip)
# sleep(3)

def random_date(start):
   current = start
   while True:
      curr = current + datetime.timedelta(minutes=randrange(600))
      yield curr



startDate = datetime.datetime(2022, 7, 18, 1, 00)

for x in (random_date(startDate)):
    start = x
    start_str = x.strftime("%d/%m/%y %H:%M")
    end = start + datetime.timedelta(minutes=randrange(60))
    end_str = end.strftime("%d/%m/%y %H:%M")
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    ip = ip if randint(0, 10) > 0 else bad_ip
    print(f"{ip} : {start_str} - {end}")
    sleep(0.5)