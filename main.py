import questions as quiz


score = 0

print("Welcome to a quiz about cat's")


if input("Do you wish to start?: ") != "yes":
    quit()

print(quiz.questions[0])
print("These are your choices: " + str(quiz.choice[0]))

if input() == quiz.answers[0]:
    print("Correct")
    score += 1

else:
    print("Wrong!")

print(quiz.questions[1])
print("These are your choices: " + str(quiz.choice[1]))

if input() == quiz.answers[1]:
    print("Correct")
    score += 1

else:
    print("Wrong!")

print(quiz.questions[2])
print("These are your choices: " + str(quiz.choice[2]))

if input() == quiz.answers[2]:
    print("Correct")
    score += 1

else:
    print("Wrong!")

print(quiz.questions[3])
print("These are your choices: " + str(quiz.choice[3]))

if input() == quiz.answers[3]:
    print("Correct")
    score += 1

else:
    print("Wrong!")

print(quiz.questions[4])
print("These are your choices: " + str(quiz.choice[4]))

if input() == quiz.answers[4]:
    print("Correct")
    score += 1

else:
    print("Wrong!")

print(quiz.questions[5])
print("These are your choices: " + str(quiz.choice[5]))

if input() == quiz.answers[5]:
    print("Correct")
    score += 1

else:
    print("Wrong!")

print(quiz.questions[6])
print("These are your choices: " + str(quiz.choice[6]))

if input() == quiz.answers[6]:
    print("Correct")
    score += 1

else:
    print("Wrong!")

print(quiz.questions[7])
print("These are your choices: " + str(quiz.choice[7]))

if input() == quiz.answers[7]:
    print("Correct")
    score += 1

else:
    print("Wrong!")

print(quiz.questions[8])
print("These are your choices: " + str(quiz.choice[8]))

if input() == quiz.answers[8]:
    print("Correct")
    score += 1

else:
    print("Wrong!")

print(quiz.questions[9])
print("These are your choices: " + str(quiz.choice[9]))

if input() == quiz.answers[9]:
    print("Correct")
    score += 1

else:
    print("Wrong!")


if score == 10:
    print("Wow you most adore cat's")
elif score == 9:
    print("You really know a lot about cat's")
elif score == 8:
    print("You are a big fan of cat's")
elif score == 7:
    print("You are a fan of cat's")
elif score == 6:
    print("You like cat's")
elif score == 5:
    print("You don't care about cat+s, but you know a bit about them")
elif score == 4:
    print("You don't like cat's")
elif score == 3:
    print("You really don't like cat's")
elif score == 2:
    print("Dog person")
elif score == 1:
    print("You despise cat's!")
elif score == 0:
    print("...")