# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name = name1 + name2

lower_combined_name = combined_name.lower()

t = lower_combined_name.count("t")
r = lower_combined_name.count("r")
u = lower_combined_name.count("u")
e = lower_combined_name.count("e")

true = t + r + u + e

l = lower_combined_name.count("t")
o = lower_combined_name.count("t")
v = lower_combined_name.count("t")
e = lower_combined_name.count("t")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90 :
 print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <=50 :
    print(f"Your score is {love_score}, you are alright together.")
else :
  print(f"Your score is {love_score}.")

