# imports
from check_cpu import check_cpu
from check_ram import check_ram
from check_uptime import check_uptime

# main variable defining.
ram = check_ram()
cpu = check_cpu()
uptime = check_uptime()

# printing output.
print(f"{ram}\n {cpu}\n {uptime}\n")
