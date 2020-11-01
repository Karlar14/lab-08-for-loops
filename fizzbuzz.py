for x in range(1, 100, 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i," fizzbuzz\r")
    elif i % 3 == 0:
        print(i," fizz")
    elif i % 5 == 0:
        print(i," buzz")
    else:
        print(i,"\r")
