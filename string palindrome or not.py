def rev(s):
    return (s==s[::-1])

s = str(input("Enter the string to check for palindrome: "))
res = rev(s)
if res is True:
    print("String is palindrome")
else:
    print("not a palindrome")
