func longestCommonPrefix(strs []string) string {
    prefix := strs[0]

    for _, s := range strs {
        i := 0
        for ; i<len(s) && i<len(prefix) && s[i] == prefix[i]; i++ {}
        prefix = prefix[:i]
    }
    return prefix
}
