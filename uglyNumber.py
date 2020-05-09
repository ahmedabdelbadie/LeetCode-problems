def uglyList():
    prime_list = [2, 3, 5]
    ugly_list = []
    for n in range(20):
        for p in prime_list:
            if n+1 % p == 0 or n+1 == 1:
                ugly_list.append(n+1)
                break
    return ugly_list


class Solution(object):
    def uglyNumber(self):
        return uglyList()


print("ugly list ",Solution().uglyNumber())
