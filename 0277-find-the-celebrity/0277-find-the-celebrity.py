# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = -1
        pot_celebrity_list = []
        for j in range(n):
            celebrity = j
            for i in range(n):
                if not knows(i, j):
                    celebrity = -1
                    break
            if celebrity != -1:
                pot_celebrity_list.append(celebrity)
        
        print(pot_celebrity_list)

        for x in range(len(pot_celebrity_list)):
            pot_celeb = pot_celebrity_list[x]
            for j in range(n):
                if j != pot_celeb and knows(pot_celeb, j):
                    pot_celebrity_list[x] = -1
            
        celebrity_list = []
        for pot_celeb in pot_celebrity_list:
            if pot_celeb != -1:
                celebrity_list.append(pot_celeb)


        if len(celebrity_list) == 1:
            return pot_celebrity_list[0]
        
        return -1

        