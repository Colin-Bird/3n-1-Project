import matplotlib.pyplot as plt
from PIL import Image
import time

def program(userInput): #A function is created to seperate the calculations from the user inputting the number
    loop = 0 # This states that loop will always start a zero when the program is restarted

    while True:
        if userInput == 1: # This states that if the user enters 1 then it will continue the code without an error
            pass

        else: #This else statement is where the calculations are done on the user input as well as noting the amount of loops that are completed to get to 1
            loop+=1
            if (userInput%2) == 0:
                userInput = userInput/2

            else:
                userInput = userInput*3+1
            continue

        return loop
        break


while True: # All the code within this while statement allow the user to input the number they want while also telling them they have put an invaldi input if the number inputted is zero or below
    try:
        while True:
            userInput = int(input("enter a number: "))
            if userInput > 0:
                break
            else:
                print("Invalid input")
                continue
        pass
    except:
        print("Invalid input")
        continue

    program(userInput)
    break


userRange = int(input("Enter a number: "))

rangeArray = []
numberArray = []

start = time.perf_counter()

for i in range(0, userRange):
    rangeArray.append(program(i+1))
    numberArray.append(i+1)

print(rangeArray)
print(numberArray)

y = rangeArray
x = numberArray

plt.bar(x,y)
plt.ylabel("Loop Count")
plt.xlabel("Numbers")

plt.savefig("barchart.png")
print("Total time taken:")

totalTime = time.perf_counter() - start

print(round(totalTime,2))

openImage = Image.open("barchart.png")
openImage.show()

exit()

