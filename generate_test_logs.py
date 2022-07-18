import random
from random import randrange, randint
import datetime 
# Format: ip.ip.ip.ip - HH:MM:SS - HH:MM:SS


ips = [".".join(map(str, (random.randint(0, 255) for _ in range(4)))) for i in range(100)]




def random_date(start,l):
   current = start
   while l >= 0:
      curr = current + datetime.timedelta(minutes=randrange(600))
      yield curr
      l-=1



startDate = datetime.datetime(2022, 7, 18, 1, 00)

for i, x in enumerate(sorted(random_date(startDate,100))):
    start = x
    start_str = x.strftime("%d/%m/%y %H:%M")
    end = start + datetime.timedelta(minutes=randrange(60))
    end_str = end.strftime("%d/%m/%y %H:%M")
    ip = ips[i-1] if randint(0, 10) > 0 else ips[99]
    print(f"{ip} : {start_str} - {end_str}")