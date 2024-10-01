def merge_overlapping_subinterval(arr):
    
    n = len(arr)
    arr.sort()
    ans = []
    for i in range(n):
        if not ans or (arr[i][0] >= ans[-1][1]):
            ans.append(arr[i])
        else:
            ans[-1][1] = max(ans[-1][1] , arr[i][1])
    return ans

arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
ans = merge_overlapping_subinterval(arr)
print("The merged intervals are:")
for it in ans:
    print(f"[{it[0]}, {it[1]}]", end=" ")
print()