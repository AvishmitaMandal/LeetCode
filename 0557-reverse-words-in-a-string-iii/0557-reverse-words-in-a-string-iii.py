class Solution:
    def reverseWords(self, s: str) -> str:
        start, end = 0, len(s)-1
        word_start, word_end = 0, 0

        string = ''

        while word_end <= end :
            # print(word_end)
            while word_end <= end and s[word_end] != ' ':
                word_end += 1
            string += s[word_start:word_end][::-1]
            string += ' '
            word_start = word_end + 1
            word_end += 1

        return string[:len(string)-1]

            
        