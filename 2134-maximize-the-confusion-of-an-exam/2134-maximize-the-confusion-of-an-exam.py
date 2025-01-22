class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        T_count, F_count = 0, 0
        start, end = 0, 0
        max_length = 0

        while end < len(answerKey):
            if answerKey[end] == 'F':
                F_count += 1
            else:
                T_count += 1
        
            while F_count > k and T_count > k:
                if answerKey[start] == 'F':
                    F_count -= 1
                else:
                    T_count -= 1
                start += 1

            max_length = max(max_length, T_count+F_count)
            end += 1

        return max_length


            

        