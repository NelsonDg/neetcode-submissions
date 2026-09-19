class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res , i, = [] , 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j]) # goes up to string from i -> j not including j
            res.append(s[j + 1 : j + 1 + length]) # j + 1 starts a dilimenter(#) and then j+1+length goes to the end of the string 
            i = j + 1 + length # This starts at the next word
        return res