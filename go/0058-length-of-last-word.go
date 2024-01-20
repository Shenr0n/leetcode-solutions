func lengthOfLastWord(s string) int {
    last := len(s)-1
    length := 0

    for s[last] == ' '{
        last--
    }

    for last>=0 && s[last] != ' ' {
        length++
        last--
    }

    return length
}
