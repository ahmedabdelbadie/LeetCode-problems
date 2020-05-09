def numbur_square(x):
    if(len(x) == 1):
        return pow(int(x), 2)
    else:
        return numbur_square(x[0]) + numbur_square(x[1:])


def verrify_happy(x):
    x = str(x)
    int_List = []  
    while 1:
        x=numbur_square(str(x))
        if(int(x) == 1):
            return True
        if str(x) in int_List:
            return False
        int_List.append(str(x))
   
class Solution(object):
    def isHappy(self, n):
        return verrify_happy(n)


print(Solution().isHappy(int(input("number : "))))
