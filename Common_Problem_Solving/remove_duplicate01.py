# def remove_duplocate(nums): 
#     unique_list = [10, ] 
#     for i in range(len(nums)): 
#         print("outer loop ====>", i) 
#         is_duplicate = False
#         for j in range(i): 
#             print( "inner loop" , j)
#             if nums[i] == nums[j]: 
#                 is_duplicate = True
#                 break

#         if not is_duplicate:
#             unique_list.append(nums[i])  
        
        
#     print(unique_list)



# nums = [10, 20, 30, 10, 30, 40, 50]
# remove_duplocate(nums)


# way two
# def remove_duplocate(nums): 
#     unique_list = []
#     for item in nums:
#         if item not in unique_list:
#             unique_list.append(item)

       
#     print(unique_list)


# nums = [10, 20, 30, 10, 30, 40, 50]
# remove_duplocate(nums)


# way three
# def remove_duplocate(nums): 
#     print(list(dict.fromkeys(nums)))

# nums = [10, 20, 30, 10, 30, 40, 50]
# remove_duplocate(nums)




# way three
def remove_duplocate(nums): 
    unique_list = []
    seen = set()

    for item in nums:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)

    print(unique_list)
    print(seen)
nums = [10, 20, 30, 10, 30, 40, 50]
remove_duplocate(nums)

