max_palindrome = 0
for i in range(999,99,-1):
    for j in range(999,99,-1):
        sum = i * j
        if(sum < max_palindrome):
            break
        if(str(sum) == str(sum)[::-1]) and sum > max_palindrome:
            max_palindrome = sum
print(max_palindrome)