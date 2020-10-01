def CheckPalindrome(word):
    for i in range(0,int(len(word)/2)):
        if(word[i]!=word[len(word)-i-1]):
            return False
        return True

word=input()
if(CheckPalindrome(word.lower())):
    print("Yes")
else:
    print("No")
