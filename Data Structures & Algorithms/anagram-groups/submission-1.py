class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in hash_map.keys():
                hash_map[sorted_str].append(str)
            else:
                hash_map[sorted_str] = [str]
        return list(hash_map.values())

