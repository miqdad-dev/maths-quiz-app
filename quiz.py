print("Welcome to Maths Quiz where your answer become your opponent")
score = 0 
mynum = int(input()) 
q1 = f"What is  :mynum  + 5?"
print(q1)
correct = mynum + 5
ans= int(input("Your answer: ")) 

if (ans == correct) :
    score +=1
else:
     score = 0 
print(f"You got  {score}  out of 5")

q2 = "What is 15-5" 
print(q2)
ans2 = int(input("Your answer: ")) 
if (ans2 == 10) :
     score +=1 
else:
    score -=1 
print(f"You got  {score}  out of 5")

q3 = "What is 5*2"
print(q3)
ans3 = int(input("Your answer: ")) 
if (ans3 == 10) :
     score +=1 
else:
    score -=1 
print(f"You got  {score}  out of 5")

q4 = "What is 10/5" 
print(q4)
ans4 = int(input("Your answer: ")) 
if (ans4 == 2) :
    score +=1
else:
    score -=1 
print(f"You got  {score}  out of 5")


print("Thanks for playing!")

