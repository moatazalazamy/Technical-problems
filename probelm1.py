def minDifference(x):
    x.sort()
    diff = 10**20
    n = len(x)
    for i in range(len(x)-1):
        if x[i+1] - x[i] < diff:
            diff = abs(x[i+1] - x[i])
    
    return diff


input("Enter array length: ")
arr = None
data = input("")
arr = list(map(int,data.split(" ")))

print(minDifference(arr))