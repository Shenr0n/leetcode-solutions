func Max(x, y int) int {
	if x <= y {
		return y
	}
	return x
}

func maxProfit(prices []int) int {
    var buy int
    var maxProfit int
    var profit int
    for sell:=1; sell<len(prices);sell++ {
         profit = prices[sell] - prices[buy]
         if profit>0{
             maxProfit = Max(maxProfit,profit)
         } else {
             buy = sell
         }
    }
    return maxProfit
}
