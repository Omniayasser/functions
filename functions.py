#function 1 to show the list
def show_menu():
    print(" (1) Check prime")
    print(" (2) Check palindrome")
    print(" (3) Exit")

#function 2, prime number checker
def is_prime(num):
    if num > 1:
        for x in range (2, num):
            if (num % x)== 0:   #if the num is divisable by any number in a range(2, num -1) is not a prime
                print(num,"is not a prime number")
                break
        else:
                print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

 # function 3, check if the input is plaindrome or not
def is_plaindrome(word):
    Reversed_Word= word[::-1]
    if word== Reversed_Word:
        print(word, " is a palindrome")
    else:
        print(word," is not a palindrome")

count = 1
while count == 1: 
    show_menu()
    opperation= int(input(" Choose an opperation"))
    if opperation == 1:
        num=int(input(" enter the number you want to check"))
        is_prime(num)
    elif opperation == 2:
        word=str(input(" enter anything you want to check"))
        is_plaindrome(word)
    elif opperation == 3:
        print(" thank you :)")
        count+=1 #change the condition to stop while loop and exit the a program
    else:
        print(" invalid input, try again. ")
