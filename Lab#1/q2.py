text = input()
Upper , Lower = 0,0
for i in text:
    if i.islower(): Lower+=1
    if i.isupper(): Upper+=1
    # print(i,end="") Just want to know what i value
print(Lower,Upper,sep="\n")