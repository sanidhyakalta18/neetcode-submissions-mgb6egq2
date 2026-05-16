class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        hashmap = defaultdict(list)

        for s in strs:
            key = " ".join(sorted(s))
            hashmap[key].append(s)

        return list(hashmap.values())