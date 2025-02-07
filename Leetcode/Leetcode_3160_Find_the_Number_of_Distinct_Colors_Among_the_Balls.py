from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        balls, colors = {},{}
        for ball, color in queries:
            if ball in balls:
                old_color = balls[ball]
                balls[ball] = color
                colors[color] = colors.get(color,0)+1
                colors[old_color] = colors.get(old_color)-1
                if colors[old_color] == 0:
                    del colors[old_color]
            else:
                balls[ball] = color
                colors[color] = colors.get(color,0)+1
            res.append(len(colors))
        return res

