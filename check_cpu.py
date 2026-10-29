# imports
import psutil
from check_status import check_status
# Alter whether or not to see each logical processer.
show_lp = False

# main func grabs the cpu information using psutill and formats it into a more readable output; which is returned 
def check_cpu():
    # basic variables and finding their values.
    uti = psutil.cpu_percent(interval=1, percpu=True)
    average = sum(uti) / len(uti)
    lp = len(uti)
    busiest_core = max(uti)
    # status checks
    status = check_status(average)
    bc_status = check_status(busiest_core)   
    # defining the dict and returning it.
    cpu = {"Name": "check_cpu", "Status": status, "average": round(average, 2), "busiest_core": (f"{bc_status} at {busiest_core}"), "total_lp": lp,}
    if show_lp:
        cpu = cpu | {"logical processer utilization": uti}
    return cpu

    
