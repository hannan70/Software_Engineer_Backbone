
const numbers = [3, 44, 38, 1, 27, 2, 4]

// first iteration --> 


// outer loop for all numbers

for(let i = 0; i < numbers.length - 1; i++) {

    let min_index = i

    // inner loop for find the min index
    for(let j = i + 1; j < numbers.length; j++) {
        if(numbers[j] < numbers[min_index]) {
            min_index = j
        }
    }  
    
    // swap two numbers
    if(min_index != i) {

        [numbers[i], numbers[min_index]] = [numbers[min_index], numbers[i]]

        // let temp = numbers[i]
        // numbers[i] = numbers[min_index]
        // numbers[min_index] = temp
    }
}

for(let i of numbers) {
    console.log(i)
}