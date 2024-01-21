func isValidSudoku(board [][]byte) bool {
    var columnCheck [9][9]bool
    var rowCheck [9][9]bool
    var gridCheck [9][9]bool

    for i, row := range board {
        for j, k := range row {
            if k == '.'{
                continue
            }
            val, err := strconv.Atoi(string(k))
            if err == nil {
                val--
                if rowCheck[i][val] || columnCheck[j][val] || gridCheck[i/3*3 + j/3][val] {
                    return false
                }
                rowCheck[i][val], columnCheck[j][val], gridCheck[i/3*3 + j/3][val] = 
                true,true,true
            }
        }
    }
    return true
}
