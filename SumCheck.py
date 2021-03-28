#Given an array of integers and a value , determine if there are any two integers in the array whose
# sum is equal to the given value . return true if sum exists else return false .

def check(arr , n):
    l = len(arr)
    for i in range(l):
        for j in range(i+1,l):
            if (arr[i] + arr[j])==n:
                return True
    return False

arr = [2,5,7,9,1]
n = int(input("enter a no.:"))

if check(arr , n):
    print("true")
else:
    print("false")

