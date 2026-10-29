import time 
import psutil


def check_uptime():
    # Raw second's answer 
    uptime = time.time() - psutil.boot_time()
    # readablility
    minutes, seconds = divmod(uptime, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    time_up = {"weeks": weeks, "days": days, "hours": hours}
    uptime = {"Name": "check_uptime",  "Status": "", "time_up": time_up}
    return uptime


