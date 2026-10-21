# imports
from check_cpu import check_cpu
from check_ram import check_ram

# main variable defining.
ram = check_ram()
cpu = check_cpu()

# printing output.
print(f"{ram}\n {cpu}\n")
