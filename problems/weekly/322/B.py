class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        chemistry = 0
        val = sum(skill) / (n // 2)
        if not val.is_integer():
            return -1

        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != val:
                return -1

            chemistry += skill[i]*skill[n - 1 - i]

        return chemistry
        
        
