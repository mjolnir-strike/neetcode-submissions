class Solution:
    def encode(self, strs: List[str]) -> str:
        encode = ""
        for string in strs:
            encode += str(len(string)) + "#" + string
        return encode

    def decode(self, s: str) -> List[str]:
        i = 0
        decode = []
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            current_len = int(s[i:j])
            end = j + 1 + current_len
            string = s[j + 1:end]
            i = end
            decode.append(string)
        return decode