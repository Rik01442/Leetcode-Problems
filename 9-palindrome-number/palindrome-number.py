class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y = x
        rem = 0
        num = 0
        while y>0:
            rem = y%10
            print(rem,num,y)
            num = num*10 + rem
            print(num)
            y =y//10
        if x==num:
            return True
        else:
            return False