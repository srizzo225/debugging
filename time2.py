#SR edited 2020-07-25
str_time = input("What time is it now (in hours 0-23)? ")
str_wait_time = input("What is the number of hours to wait? ")
time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = time + wait_time
#need to adjust time when it goes past 24
alarmtime = time_when_alarm_go_off % 24
print(alarmtime)
