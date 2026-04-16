#  Approach 1: String Slicing

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index == -1:
            return word
        return word[index:: -1] + word[index+1:]

        
# Approach 2: Two Pointers (In-place Simulation)

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word_list = list(word)
        index = -1

        for i in range(len(word_list)):
            if word_list[i] == ch:
                index = i
                break

        if index == -1:
            return word

        l, r = 0, index
        while l < r:
            word_list[l], word_list[r] = word_list[r], word_list[l]
            l += 1
            r -= 1

        return "".join(word_list)