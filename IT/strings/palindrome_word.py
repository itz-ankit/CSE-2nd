s=input("Enter a word: ")

## ans = (s == s[::-1])

for i in range(0, int(len(s)/2)):
	if s[i] != s[len(s)-i-1]:
		ans=False
ans= True

if ans:
	print("Yes")
else:
	print("No")

'''
Enter a word: malayalam
Yes

'''