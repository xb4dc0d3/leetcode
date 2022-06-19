class Solution:
    def isHappy(self, n: int) -> bool:

        ans = n
        str_n = str(n)
        
        
        if ans == 1 or ans == 7:
            return True

       
        while ans > 9:

            ans = 0
            for idx in range(len(str_n)):
                ans += (int(str_n[idx]) ** 2)
            str_n = str(ans)



        # check if in range 2 < 9
        if ans == 7 or ans == 1:
            return True

        return False
