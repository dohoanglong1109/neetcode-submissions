class Solution:
    def encode(self, strs: List[str]) -> str:
        send = ""
        for s in strs:
            n = len(s)
            send += (str(n) + "#" + s)

        return send
    def decode(self, s: str) -> List[str]:
        num = ""
        result = []
        i = 0
        while i < len(s):
            if s[i] != "#":
                num += s[i]
                i += 1
            if s[i] == "#":
                jump = int(num)
                result.append(s[i+1:i+jump+1])
                i += (jump+1)
                num = ""

        return result