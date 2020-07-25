from turtle import *
def turtle_controller(tun, wert):
    tun = tun.upper()
    if tun == "V":
        forward(wert)
    elif tun == "Z":
        backward(werd)
    elif tun == "R":
        right(wert)
    elif tun == "l":
        left(wert)
    elif tun == "A":
        penup()    
    elif tun == "E":
        pendown()
    elif tun == "N":
        reset()
    else:
        print("Unbekannter Befehl")
