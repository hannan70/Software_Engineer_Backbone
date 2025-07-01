let arr = [30, 17, 1, 15, 2, 100, 12, -1]


for(let i = 0; i < arr.length-1; i++) {
    for(let j = 0; j < arr.length-1-i; j++) {
        if(arr[j] > arr[j+1]){
            [arr[j], arr[j+1]] = [arr[j+1], arr[j]]
        }
    }
}

for(let i of arr) {
    console.log(i)
}