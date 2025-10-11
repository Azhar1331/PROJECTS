from random import randint

n = randint(1,100)
a = -1
guesses = 1

while(a != n):
  a  = int(input("Enter the number (between 1 to 100) : "))
  
  if (a > n):
    print("Lower Number please")
    guesses += 1
  elif(a < n):
    print("Higher number please")  
    guesses += 1
    
print(f"Congrats you guessed the number {n}  correctly in {guesses} guesses")    