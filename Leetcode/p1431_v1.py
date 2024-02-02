def kidsWithCandies(self, candies, extraCandies):
    max_candies = max(candies)
    added_candies = [candy+extraCandies for candy in candies]
    result = [bool(1) if candy>=max_candies else bool(0) for candy in added_candies]
    return(result)