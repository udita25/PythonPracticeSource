def findmissing(arr, n):
    total = (n*(n+1))/2
    sum = 0
    for i in range(n-1):
        sum += arr[i]
    
    return total - sum

# Driver code
arr = [1, 2, 4, 5, 6]
n = len(arr)

missingnum = findmissing(arr, n)
print("Missing number is", missingnum)

