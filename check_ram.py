import psutil 
gig = 1024**3
meg = 1024**2


def byte_CON(num_bytes):
    gigabyte, leftover = divmod(num_bytes, gig)
    meg_remainder = leftover // meg
    return gigabyte, meg_remainder


def check_ram():
    mem = psutil.virtual_memory()
    total = byte_CON(mem.total)
    used = byte_CON(mem.used)
    status = ""
    percent = mem.percent
    if percent <= 50:
        status = "Ok " + str(percent)
    elif percent > 50 & percent <= 80:
        status = "Warning " + str(percent)
    elif percent > 80:
        status = "Critical " + str(percent)
    Ram = {"total": str(total), "used": str(used), "status": status}
    return Ram

ram = check_ram()
    
print(ram)        



