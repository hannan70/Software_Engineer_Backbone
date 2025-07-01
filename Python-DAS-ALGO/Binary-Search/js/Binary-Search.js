
function binary_search(arr, item){
    let left = 0
    let right = arr.length - 1
    while(left <= right){
        middle = Math.floor((left + right) / 2)
        if(arr[middle] === item) {
            return middle
        }
        else if(arr[middle] < item) {
            left = middle + 1
        }
        else {
            right = middle - 1
        }
    }
    return -1;
}


numbers_arr = [10, 20, 30, 40, 50, 60]
target = 60

let index = binary_search(numbers_arr, target)

if(index === -1){
    console.log(`Item not found`)
}
else {
    console.log(`Item found at index ${index}`)
}