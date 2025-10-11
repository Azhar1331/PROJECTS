import random
'''
1 for snake
-1 for water
0 for gun
'''
youDict = {"snake" : 1 , "water" : -1, "gun" : 0}

reversedDict = {  1 :"snake"  ,-1 : "water" ,  0 :"gun" }

computer = random.choice(list(reversedDict.keys()))

youStr = input("Enter your choice ( water , snake ,  gun): ").lower()


if youStr not in youDict:
  print("Invalid choice. Please enter 'snake', 'water', or 'gun'.")
else:    
  youNum = youDict[youStr]
  print(f" You  chose {reversedDict[youNum]}  \n Computer Chose {reversedDict[computer]}")
  
  
  if computer == youNum:
        print("🎉 It's a Draw! 🎉")
  elif (youNum == 1 and computer == -1) or \
      (youNum == 0 and computer == 1) or \
      (youNum == -1 and computer == 0):
   print("🏆 You Win! 🏆")
        
  else:
    print("😭 You Lose! 😭")

  # if(computer ==  youNum):
  #   print(" It's a Draw!")
  # else:
  #   if(computer ==  -1 and youNum == 1):
  #     print("You Win!")
  #   elif(computer ==  1 and youNum == 0):
  #     print("You Win!")
  #   elif(computer ==  0 and youNum == -1):
  #     print("You Win!")
  #   elif(computer ==  -1 and youNum == 0):
  #     print("You Lose!")
  #   elif(computer ==  0  and youNum == 1):
  #     print("You Lose!")
  #   elif(computer ==  1 and youNum == -1):
  #     print("You Lose!")
  #   else:
  #     print("Something went wrong ")  