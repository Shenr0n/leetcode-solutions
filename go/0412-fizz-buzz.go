func fizzBuzz(n int) []string {
    
    answer := make([]string,0)

    for i:=1; i<=n; i++ {
        if i%3==0 && i%5==0 {
            answer = append(answer,"FizzBuzz")
            continue
        }
        if i%3==0 {
            answer = append(answer,"Fizz")
        } else if i%5==0{
            answer = append(answer,"Buzz")
        } else {
            answer = append(answer,strconv.Itoa(i))
        }
    }
    return answer
}
