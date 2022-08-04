# Find the  misssing one in the list of an array...
arr = [1,4,3,2,5,7,9,8]

sort_arr = sorted(arr)
print(sort_arr)

first = 0 
last = 1

for i in range(len(arr)):
    if sort_arr[last] - sort_arr[first] == 1:
        first =first+1
        last =last +1
    else :
        val = sort_arr[first]+1

print(val," is missing...")