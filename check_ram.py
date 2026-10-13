import psutil 
gig = 1024**3
meg = 1024**2


def byte_CON(num_bytes):
    gigabyte, leftover = divmod(num_bytes, gig)
    meg_remainder = leftover // meg
    return gigabyte, meg_remainder


def check_ram():
    mem = psutil.virtual_memory()
    total1, total2 = byte_CON(mem.total)
    used1, used2 = byte_CON(mem.used)
    status = ""
    percent = mem.percent
    if percent <= 50:
        status = "Ok"
    elif percent <= 80:
        status = "Warning"
    else:
        status = "Critical"
    Ram = {"name": "check_ram", "total": str(f"{total1} GB, {total2} MB"), "used": str(f"{used1} GB, {used2} MB"), "status": status, "percent": percent}
    return Ram




