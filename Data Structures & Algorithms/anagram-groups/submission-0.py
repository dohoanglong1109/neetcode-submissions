class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for s in strs:
            temp = "".join(sorted(s))

            if temp in anagram_dict:
                        anagram_dict[temp].append(s)

            if temp not in anagram_dict:
                anagram_dict[temp] = [s]        

        result = []
        for values in anagram_dict.values():
            result.append(values)

        return result