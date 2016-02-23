#Program 1 Formatted OutPut

# By: Mason Perry

###                     2.1 Drawing Pyramids                      ###
#to get the range between numbers
for k in range(1,5+1):
    print(k)

###                     2.2 Half Pyramid                          ###
#Ask user input
print("2.2 A half Pyramid!")
height = int(input("How many levels of the pyramid would you like to have?  "))
print("Pyramid of Pound signs")
for level in range (1, height+1):       #For loop gives height of half pyramid
    for n in range (level - height):    #for loop decrements levels
        print("#", end = " ")
    for n in range (0, level):          #For loop starting from zero
        print("#", end = " ") 
    print(" ")



###                     2.3 The Full Pyramid                     ###             
#Ask user input
print("2.3 A Full Pyramid")
height = int(input("How many levels of the pyramid would you like to have? "))

#prints a full pyramid using height
print("Pyramid of Pound Signs")
for level in range (1 , height+1):      #For Loop for height
    for n in range (height - level):    #For Loop for decrementing the height by level
        print(" ", end = " ")
    for n in range (1, level):          #For Loop adds to level
        print("#", end = " ") 
    for level in range (level, 0, -1):  #For Loop ends the level of pyramid
        print("#", end = " ")
    print(" ")


###                    3.1 Right Side Parabola                       ###

#Ask User Input
height = int(input("Enter how high you would like your parabola: "))

x=2
y=(x**2)/4

#set height to user input; note x_max can be used as a variable for the user input
x_max = height

#for loop that connects user input 
for x in range(-x_max, x_max +1):
    x = int((x**2)/4)
    print(" "*x+"V")

