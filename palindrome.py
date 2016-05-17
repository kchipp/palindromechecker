def whatIsTheWord():
    enterWord = input("Please enter the word ")
    enterWord = enterWord.lower()
    return enterWord
    
def checkPalindrome(n):
    rightIndex = len(n)-1
    leftIndex = 0
    while leftIndex < rightIndex:
        if n[leftIndex] ==n[rightIndex]:
            print("These letters matched")
           
        else:
            print ("It's not a palindrome")
            return False
        rightIndex = rightIndex - 1
        leftIndex +=1  
    return True        

def displayResults(palindromeResult):
    if palindromeResult == True:
        print("Congrats, it's a Palindrome!")    
    elif palindromeResult == False:
        print("Oh No, it's not a Palindrome")

def main():
    print ("Is it a Palindrome?")
    enterWord = whatIsTheWord()
    isPalindrome = checkPalindrome(enterWord)
    displayResults(isPalindrome)
    
    
if __name__ == "__main__":
    main()