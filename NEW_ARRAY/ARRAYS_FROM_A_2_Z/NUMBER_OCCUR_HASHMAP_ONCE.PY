def occur(arr):
    
    hashmap = {}
    
    for num in arr:
        hashmap[num] = hashmap.get(num,0) +1
        
    for num,count in hashmap.items():
        if(count == 1):
            return num
    return -1

arr = [4, 0, 1, 1, 4]
ans = occur(arr)
print("The single element is:", ans)