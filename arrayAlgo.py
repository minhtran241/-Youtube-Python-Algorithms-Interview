'''
1. Array Pair Sum:
Given an integer array, output all the unique
pairs that sum up to a specific value k. 

So the input:
pair_sum([1, 3, 2, 2], 4)
would return 2 pairs:
(1, 3)
(2, 2)

'''

def pair_sum(array, k):
    if len(array) < 2:
        return None

    seen = set()
    output = set()
    
    for num in array:
        target = k - num
        if target not in seen: 
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
    return '\n'.join(map(str, output))

'''

2. Largest continuous sum:
Take an array with positive and negative integers 
and find the maximum continuous sum of that array

'''

def largest_continuous(arr):
    if len(arr == 0):
        return None
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum 

'''
3. Rotation:
Given 2 arrays (assume no duplicates)
is 1 array a rotation of another - return True/False
same size and elements but start index is different

Ex:
[1, 2, 3, 4, 5, 6, 7]
[4, 5, 6, 7, 1, 2, 3]

'''

def is_rotation(list1, list2):
    if len(list1) != len(list2):
        return False
    
    length = len(list1)
    key = list1[0]
    key_index = -1

    for i in range(length):
        if list2[i] == key:
            key_index = i
            break

    if key_index == -1:
        return False

    for i in range(length):
        j = (key_index + i) % length
        if list1[i] != list2[j]:
            return False
    return True

'''
4. Common elements in 2 sorted arrays:
Return the common elements (as an array) between 2
sorted arrays of integers ascending order
Example: The common elements between:
[1, 3, 4, 6, 7, 9] and [1, 2, 4, 5, 9, 10]
are [1, 4, 9]

'''

def common_elements(list1, list2):
    common = []
    pointer1 = pointer2 = 0
    while pointer1 < len(list1) and pointer2 < len(list2):
        if list1[pointer1] == list2[pointer2]:
            common.append(list1[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif list1[pointer1] > list2[pointer2]:
            pointer2 += 1
        else:
            pointer1 += 1
    
    while pointer1 < len(list1):
        if list1[pointer1] == list2[pointer2 - 1]:
            common.append(list1[pointer1])
        pointer1 += 1

    while pointer2 < len(list2):
        if list1[pointer1 - 1] == list2[pointer2]:
            common.append(list2[pointer2])
        pointer2 += 1
        
    return common

'''
5. Minesweeper: 
Cho trước bombs là 1 nested list gồm toạ độ các bomb, số row and col
Nhiệm vụ: Phải update những cell xung quanh mỗi bomb lên +1 để 
khi đi đến cell đó ta biết được xung quanh cell đó có mấy bomb

return về 1 nested list như 1 field, 0 là 0 có bomb, -1 là bomb

'''

def mine_sweeper(bombs, num_rows, num_cols):
    # update the initial condition of field
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    for bomb_location in bombs:
        [bomb_row, bomb_col] = bomb_location
        field[bomb_row][bomb_col] = -1

        # update the cells around current bomb +1
        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col - 1, bomb_col + 2)

        for i in row_range:
            for j in col_range:
                if 0 <= i < num_rows and 0 <= j < num_cols and field[i][j] != -1:
                    field[i][j] += 1
    return field

'''
6. Frequent count:
Given an array what is the most frequent occuring elements
'''

def most_frequent(list):
    count = {}
    max_count = 0
    max_item = None

    for item in list:
        if item not in count:
            count[item] = 1
        else: 
            count[item] += 1
        if count[item] > max_count:
            max_count = count[item]
            max_item = item

    return max_item




    


    
