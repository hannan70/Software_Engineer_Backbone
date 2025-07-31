
function findZigZagSequence(arr, n) {
    let flag = true
    for(let i = 0; i < n-1; i++) {
        if(flag){
            if(arr[i] > arr[i+1]) {
                let temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            }
        }
        else {
            if(arr[i] < arr[i+1]) {
                let temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            }
        }
        flag = !flag
    }
    return arr;
}

arr = [3, 4, 6, 2, 1, 8, 9]
n = arr.length
findZigZagSequence(arr, n)
for(let i of arr){
    console.log(i)
}