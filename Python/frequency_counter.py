l=list(map(int,input("Enter the elements of the list separated by space: ").split()))
freq_dict={}
for num in l:
    if num in freq_dict:
        freq_dict[num]+=1
    else:
        freq_dict[num]=1
print("Frequency of each element in the list:")
for key, value in freq_dict.items():
    print(f"{key} occurs {value} times")