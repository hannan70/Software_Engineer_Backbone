def bubble_sort(arr):
    size = len(arr) # 5
    
    for i in range(0, size-1): # 5-1 == 4 -- 0--3
        swap = 0
        print("outer loop --", i) 
        for j in range(0, size-i-1): # 5-0-1 # 4 -- 4 loop mean 0..3 loop
            print("inner loop ", j) 
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                
                swap = 1
        print("outer loop sort", arr)
        if swap == 0:
            print("now swap found")
            break

        print("swap ====", swap)



arr = [30, 17, 1, 12, -1]


bubble_sort(arr)

for k in arr:
    print(k, end=" ")