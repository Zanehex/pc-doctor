# Imports
import psutil 
from check_ram import byte_CON
from check_status import check_status

# grabs the disk information on the defult C drive then converts the information from bytes to GB & MB; places this into a dict which is returnd 
def check_disk():
    path = "C:/"
    storage = psutil.disk_usage(path)
    # Byte conversion 
    (total) = byte_CON(storage[0])
    (use) = byte_CON(storage[1])
    (free) = byte_CON(storage[2])
    percent = storage[3]
    status = check_status(storage[3])
    # Dict making 
    disk = {"Name": "check_disk", "status": status, "total": (f"{total[0]} GB, {total[1]} MB"), "free": (f"{free[0]} GB, {free[1]} MB"), "used": (f"{use[0]} GB, {use[1]} MB"), "percent": percent}
    return disk


