class Solution:
    def isPalindrome(self, s: str) -> bool:
        index = 0
        last = len(s) - 1
        while index < last:
            while index < last and not s[index].isalnum():
                index += 1
            while index < last and not s[last].isalnum():
                last -= 1
            if s[index].lower() != s[last].lower():
                return False
            index += 1
            last -= 1
        return True
