class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = [0] * 10
        for d in digits:
            count[d] += 1
        
        result = 0
        # ones digit: even numbers
        for ones in [0, 2, 4, 6, 8]:
            if count[ones] == 0:
                continue
            count[ones] -= 1
            # hundreds digit: 1-9 (no leading zero)
            for hundreds in range(1, 10):
                if count[hundreds] == 0:
                    continue
                count[hundreds] -= 1
                # tens digit: any 0-9
                for tens in range(10):
                    if count[tens] > 0:
                        result += 1
                count[hundreds] += 1
            count[ones] += 1
        
        return result        