class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        s1=""
        for i in s:
            s1=i+" "+s1
        return s1.strip()

        