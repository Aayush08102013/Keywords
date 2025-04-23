# Take user input:
a = input ("Enter a word: ")

# program to check break keyword:
for i in a: # iterate loop
    if (i == "A"): # condition 1:
        # Display result:
        print("A is found!")
        break

    else:
        print("A was not found")

# Pass Keyword
for x in range(10): # iterate loop:
    if x % 20 == 0:
        print("The number is divisble by 20")
    elif x % 15 == 0:
        pass   # pass keyword
    elif x % 5 == 0:
        print("The number is divisble by 5")
    elif x % 3 == 0:
        print("The number is divisble by 3")
    else:
        print(x)

# Continue statement:

var = 100

while var > 0:
    var = var - 1
    if var == 5:
        continue
    # display the result:
    print('\n the current var value is', var)

print('\n Goodbbye :)!')