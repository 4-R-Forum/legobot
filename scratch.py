HeadingChange = 30

def dev_update(yaw):
    if HeadingChange > 0:
        return HeadingChange - yaw
    else:
        return HeadingChange + yaw

def turn_complete(dev):
    if HeadingChange > 0:
        if dev < 0:
            return True
        else:
            return False
  
    elif HeadingChange < 0:
        if dev > 0:
            return True
        else:
            return False

    
print (dev_update(29))
print (turn_complete(1))
print (dev_update(32))
print (turn_complete(-2))



