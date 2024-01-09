//nlogn
func distance(x, y int) int{
    return (x*x)+(y*y)
}

func kClosest(points [][]int, k int) [][]int {
    freq := make(map[int][][2]int)
    var kPoints [][2]int
    result := make([][]int,k)

    for _,point := range points {
        x,y := point[0], point[1]
        dist:=distance(x,y)
        freq[dist] = append(freq[dist], [2]int{x,y})
    }

    for key := range freq{
        kPoints = append(kPoints,freq[key]...)
    }

    sort.SliceStable(kPoints,func(i,j int)bool { 
        distI := distance(kPoints[i][0], kPoints[i][1])
        distJ := distance(kPoints[j][0], kPoints[j][1])
        return distI < distJ
    })

    for i:=0; i<k; i++{
        result[i] = []int{kPoints[i][0], kPoints[i][1]}
    }

    return result

}
