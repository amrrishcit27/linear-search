arr=[10,20,30,40,50]
key=int(input("enter the number to search:"))
for i in range(len(arr)):
    if arr[i]==key:
        print("number found at index:",i)
        break
else:
    print("number not found")