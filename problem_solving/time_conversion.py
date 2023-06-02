def timeConversion(s):
    hour = (s[:2])
    inthour = int(hour)
    ampm = s[-2:]
    body=s[2:-2]
    if ampm=="PM":
        if hour == "12":
            return s[:8]
        print("PM block")
        inthour += 12
        return str(inthour)+s[2:8]
    elif (ampm=="AM"):
        if(hour=="12"):
            return '00'+s[2:8]
        return s[:8]
        s = str(inthour)+s[2:8]
    return s
    # Write your code here
