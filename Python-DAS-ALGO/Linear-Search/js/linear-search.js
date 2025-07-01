
const linear_search = (arr, item) => {
    for(let i = 0; i <= arr.length - 1; i++){
        if(arr[i] === item) {
            return i
        }
    }
    return -1

}

let arr = [30, 22, 33, 50, 10]
// let item = 500 // item not found
let item = 22 // item found at index 1
let index = linear_search(arr, item)

if(index === -1){
    console.log(`Item not found`)
}
else {
    console.log(`Item found at index ${index}`)
}