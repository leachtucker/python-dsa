# Leetcode 242
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def getSeenDict(self, s: str) -> dict:
        seenInS = {}
        for char in s:
            if char not in seenInS:
                seenInS[char] = 1
            else:
                seenInS[char] += 1
        
        return seenInS

    def isSeenEqual(self, seenInS: dict, seenInT: dict) -> bool:
        for char, value in seenInS.items():
            if char not in seenInT:
                return False
            
            if seenInT[char] != seenInS[char]:
                return False

        return True
    
    def isAnagram(self, s: str, t: str) -> bool:
        seenInS = self.getSeenDict(s)
        seenInT = self.getSeenDict(t)
        
        if not self.isSeenEqual(seenInS, seenInT):
            return False
        
        if not self.isSeenEqual(seenInT, seenInS):
            return False
            
        return True