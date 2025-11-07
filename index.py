print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")

left_or_right = input("left or right ")
if left_or_right == "left":
    swim_or_wait = input("swim or wait ")
    if swim_or_wait == "wait":
        which_door = input("Which door? ")
        if which_door == "red":
            print("Burned by fire. Game Over. ")
        elif which_door == "yellow":
            print("You Win! ")
        elif which_door == "blue":
            print("Eaten by beasts.Game Over.")
        else:
            print("Game Over. ")
        
    else: 
        print("Attacked by trout. Game Over ")
    
else:
    print("Fall into a hole. Game Over ")
