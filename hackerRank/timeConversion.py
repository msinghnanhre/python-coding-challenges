timeString = "07:05:45PM"

def timeConversion(s):
    if s[-2:] == "AM" and s[0:2] == "12":
        return("00" + s[2:-2])
    elif s[-2:] == "PM" and s[0:2] == "12" or s[-2:] == "AM":
        return(str(s[:-2]))
    elif s[-2:] == "PM":
        return(str(int(s[:2])+12)+s[2:-2])
