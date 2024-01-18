func isSubsequence(s string, t string) bool {
    if s == "" {
        return true
    }
    first, second := len(s), len(t)
    i,j:=0, 0
    
    for i<first && j<second {    
        if s[i] == t[j] {
            i++
        }
        j++
    }
    return i == len(s)
}
