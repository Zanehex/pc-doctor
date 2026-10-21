# imports
import psutil 
from check_status import check_status
# constant variables  
gig = 1024**3
meg = 1024**2

# turns the number of bytes into gigabytes and its megabyte remainder,  
def byte_CON(num_bytes):
    gigabyte, leftover = divmod(num_bytes, gig)
    meg_remainder = leftover // meg
    return gigabyte, meg_remainder

# the main func grabs the ram information using psutill and formats it into a readable output; which is returned
def check_ram():
    # basic variable defining and finding their values.
    mem = psutil.virtual_memory()
    total1, total2 = byte_CON(mem.total)
    used1, used2 = byte_CON(mem.used)
    percent = mem.percent
    # status checks.
    status = check_status(percent)
    # defining the dict and returning it. 
    Ram = {"name": "check_ram", "total": str(f"{total1} GB, {total2} MB"), "used": str(f"{used1} GB, {used2} MB"), "status": status, "percent": percent}
    return Ram




