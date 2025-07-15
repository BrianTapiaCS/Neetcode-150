'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)

        if n != m:
            return False
        
        freqS, freqT = {}, {}

        for c in s:
            if c not in freqS:
                freqS[c] = 1
            else:
                freqS[c] += 1

        for c in t:
            if c not in freqT:
                freqT[c] = 1
            else:
                freqT[c] += 1
    
        for letter in freqS:
            if letter not in freqT or freqS[letter] != freqT[letter]:
                return False
                
        return True

