def checkOrders(dineIn, takeOut, servedOrders):
    for order in servedOrders:
        if dineIn != [] and order == dineIn[0]:
            del dineIn[0]
        elif takeOut != [] and order == takeOut[0]:
            del takeOut[0]
        else:
            return False
    return True


TOO = [1, 3, 5]
DIO = [2, 4, 6]
SO = [1, 2, 4, 6, 5, 3]

print(checkOrders(DIO, TOO, SO))

TOO = [17, 8, 24]
DIO = [12, 19, 2]
SO = [17, 8, 12, 19, 24, 2]


print(checkOrders(DIO, TOO, SO))
