class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for string in strs:
            char_freq = [0] * 26
            for s in string:
                char_freq[ord(s) - ord('a')] += 1
            
            key = tuple(char_freq)
            if key not in anagram_map:
                anagram_map[key] = []

            anagram_map[key].append(string)
        
        return list(anagram_map.values())
