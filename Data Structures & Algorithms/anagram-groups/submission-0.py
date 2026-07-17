class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_dict = defaultdict(list)

        for word in strs:
            group_dict["".join(sorted(word))].append(word)

        return list(group_dict.values())



























        # empty_dict = defaultdict(list)

        # for word in strs:
        #     empty_dict["".join(sorted(word))].append(word)

        # return list(empty_dict.values())