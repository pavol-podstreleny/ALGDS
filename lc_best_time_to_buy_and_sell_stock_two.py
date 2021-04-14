class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        localMinimas = self.findLocalMinima(prices)

        if len(localMinimas) == 0:
            return 0
        result = 0
        for i in range(1, len(localMinimas)):
            largestNumber = self.findLargestNumberInInterval(
                prices, localMinimas[i-1], localMinimas[i])
            result += largestNumber - prices[localMinimas[i-1]]

        largestNumber = self.findLargestNumberInInterval(
            prices, localMinimas[-1], len(prices))
        result += (largestNumber - prices[localMinimas[-1]])

        return result

    def findLargestNumberInInterval(self, prices, low, up):

        maximum = float("-inf")
        for i in range(low+1, up):
            if prices[i] > maximum:
                maximum = prices[i]

        return maximum

    def findLocalMinima(self, prices):

        minimas = []
        if len(prices) >= 2:
            if prices[0] < prices[1]:
                minimas.append(0)

        for i in range(1, len(prices)-1):
            prevValue = prices[i-1]
            actualValue = prices[i]
            nextValue = prices[i+1]

            if actualValue <= prevValue and actualValue < nextValue:
                minimas.append(i)

        return minimas
