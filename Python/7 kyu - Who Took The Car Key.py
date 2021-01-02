def who_took_the_car_key(message):
    x = len(message)
    mySeparator = ''
    mes = []
    for i in range(x):
        mes.append(chr(int(message[i],2)))
    return mySeparator.join(mes)


###Best Practiced Solution by vote from user
# def who_took_the_car_key(message):
#     return ''.join(chr(int(i,2)) for i in message)