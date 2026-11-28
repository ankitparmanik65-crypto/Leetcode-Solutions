class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # Greedy + Sieve (Multiples Counting) + Sorting
        
        # Sort items by price
        items.sort(key=lambda x: x[1])

        n = len(items)
        max_factor = max(factor for factor, price in items)
        min_price = items[0][1]

        # Count frequency of each factor
        freq = [0] * (max_factor + 1)

        for factor, price in items:
            freq[factor] += 1

        # Count how many factors are divisible by each factor
        total = [0] * (max_factor + 1)

        for factor in range(1, max_factor + 1):
            for multiple in range(factor, max_factor + 1, factor):
                total[factor] += freq[multiple]

        answer = 0

        # Greedily buy the cheapest boosted copies
        for factor, price in items:

            if price >= 2 * min_price:
                break

            gain = total[factor] - 1

            if gain <= 0:
                continue

            count = min(gain, budget // price)

            answer += count * 2
            budget -= count * price

        # Spend remaining budget on cheapest items
        answer += budget // min_price

        return answer
