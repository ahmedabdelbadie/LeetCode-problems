x = int(input("pattern : "))
for row in range(x):
    text = ""
    for num in range(x*2 - 1):
        if num < x:
            if(num >= (x-row)):
                text += " "
            else:
                text += str(x-num)
        else:
            if(num + 1 < (row+x)):
                text += " "
            else:
                text += str((num-x)+2)
    print(text)
