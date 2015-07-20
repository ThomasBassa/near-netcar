def interpolate():
#            ifPositive = True
#            if val[0] - oldval[0] <= 0:
#                ifPositive = False
#            print(ifPositive)
    diff = oldval[0] - val[0]
    if diff > maxTurn:
        diff = maxTurn
    elif diff < (maxTurn*-1):
        diff = maxTurn*-1
#            if ifPositive == False:
#                diff = diff * -1
    print("diff: {}".format(diff))
    axiszeroold = val[0]
    val = (axiszeroold + diff, verticalPosition)
    if val[0] >  1:
        val = (1,verticalPosition)
    elif val[0] < -1:
        val = (-1,verticalPosition)
    oldval = (horizPosition,verticalPosition)
    print("val set")
    print("Axis 0 at {}".format(val[0]))
    print("Axis 1 at {}".format(val[1]))
    print("Old 0: {}".format(oldval[0]))
    print("Old 1: {}".format(oldval[1]))
    self.call('aero.near.joyMonitor', val[0], val[1])]