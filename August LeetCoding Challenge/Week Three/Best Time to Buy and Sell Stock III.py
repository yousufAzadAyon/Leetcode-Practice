class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstbuy,firstsell=-int(1e9),0
        secondbuy,secondsell=-int(1e9),0
        for price in prices:
            firstbuy=max(firstbuy,-price)
            firstsell=max(firstsell,firstbuy+price)
            secondbuy=max(secondbuy,firstsell-price)
            secondsell=max(secondsell,secondbuy+price)
        return secondsell    