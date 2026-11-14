l=list(map(int, input("Enter numbers separated by space: ").split()))
l=list(set(l))
l.sort()
if len(l)<2:
    print("There is no second largest number.")
else:
    print("The second largest number is:", l[-2])