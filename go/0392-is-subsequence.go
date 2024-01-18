func isSubsequence(s string, t string) bool {
    first := len(s)-1
    second := len(t)-1

    if s == "" {
        return true
    }
    
    for i,j:=0,0; i<=first && j<=second; {
        
        if s[i] == t[j] {
            if i == first && j<=second {
                return true
            } else {
                i++
                j++
            }
        } else {
            j++
        }
    }
    return false
}
