func maxProfit(prices []int) int {
    var maxProfit int
    buy := prices[0]

    for i:=1; i<len(prices); i++ {
        if prices[i] < buy {
            buy = prices[i]
        } else if (prices[i] - buy) >= maxProfit {
            maxProfit = prices[i] - buy
        }
    }
    return maxProfit
}
