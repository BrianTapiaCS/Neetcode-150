'''
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            current_word = ''.join(sorted(word))
            #print(current_word)
            if current_word not in group:
                group[current_word] = [word]
            else:
                group[current_word].append(word)
        
        return [x for x in group.values()]
