
# takes the number given and then returns a str of its respected status; is assumed it will be used for numbers out of 100 and that the higher the number the worse it is.
def check_status(number):
    if number <= 50:
        variable = "ok"
    elif number <= 80:
        variable = "warning"
    else:
        variable = "critical"
    return variable