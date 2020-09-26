# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# none

def avg(user_list):
    average = sum(user_list)/len(user_list)
    return average

if __name__ == '__main__':
    # test your fucntion with this print statement before writing the input loop
    #print(avg([2, 4, 6]))    # Put the values you want to test in for x,y and z\

    # Now, comment out the print statement and work on the code below
    # Remember to indent in this section
    user_list = [] # start with an empty list
    # Write a loop to allow the user to input the values to be averaged
    num=int(input("how many numbers do you want the average of "))
    s = 1
    while num >= s:
        user_input = int(input("enter a number "))
        user_list.append(user_input)
        s +=1
    print(avg(user_list))

#DIFF WAY
#def avg(user_list):
    #average = sum(user_list)/len(user_list)
    #return average

#user_list = []
#while num != "done":
    #num = input("enter a number to be averaged. if done type done ")
    #if num == "done":
        #break
        #num=int(num)
    #user_list.append(int(num))
#print(avg(user_list)) 



