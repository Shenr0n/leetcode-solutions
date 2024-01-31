type Stack []int

func (s *Stack) Push(value int){
    *s = append(*s, value)
}

func (s *Stack) Pop(){
    if len(*s) != 0 {
        idx := len(*s)-1
        *s = (*s)[:idx]
    } else {
        return
    }
}

func calPoints(operations []string) int {

    var opStack Stack
    var sum int

    for _, op := range operations {
        if op == "+" {
            if len(opStack) >= 2 {
            opStack.Push(opStack[len(opStack)-1] + opStack[len(opStack)-2])
            } else {
                continue
            }
        } else if op == "D" {
            if len(opStack) > 0 {
                opStack.Push(2 * opStack[len(opStack)-1])
            } else {
                continue
            }
        } else if op == "C" {
            opStack.Pop()
        } else {
            val,_ := strconv.Atoi(op)
            opStack.Push(val)
        }
    }
    for _, val := range opStack {
        sum += val
    }
    return sum
}
