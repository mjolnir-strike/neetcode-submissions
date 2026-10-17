class Solution:
    def encode(self, strs: List[str]) -> str:
        encode = ""
        for string in strs:
            encode += str(len(string)) + "#" + string
        return encode

    def decode(self, s: str) -> List[str]:
        i = 0
        current_len = 0
        strlen = ""
        decode = []
        j = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            strlen = s[i:j]
            current_len = int(strlen)
            i = j + 1
            string = s[i:i+current_len]
            print(string)
            i = i+current_len
            decode.append(string)
        return decode