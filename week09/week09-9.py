 N = len(salary)

        ans = (sum(salary)-max(salary)-min(salary))/(N-2)

        return ans