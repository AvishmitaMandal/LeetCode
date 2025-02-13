class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        init_direction = (1,0)
        init_position = (0,0)
        
        direction = (1,0)
        position = (0,0)

        mp_left = {
            (1, 0) : (0, -1),
            (0, -1) : (-1, 0),
            (-1, 0) : (0, 1),
            (0, 1) : (1, 0)
        }
        
        mp_right = {
            (1, 0) : (0, 1),
            (0, 1) : (-1, 0),
            (-1, 0) : (0, -1),
            (0, -1) : (1, 0)
        }

        for i in instructions:
            if i == 'G':
                (xp, yp) = position
                (xd, yd) = direction 

                position = (xp+xd, yp+yd)
            
            elif i == 'L':
                direction = mp_left[direction]

            elif i == 'R':
                direction = mp_right[direction]

        if position != init_position and direction == init_direction:
            return False

        return True
