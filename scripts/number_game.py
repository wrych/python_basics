'''
Write a program that plays a game of numbers. 
The first input is going to be the magic number. 
After that, the players need to count upwards (i.e. 1, 2, 3 etc.). 
Whenever the number is divisible or has the magic number in it, the player needs to write either “muh” or “meh”. 
If the the player gives the wrong number or a number when he should be typing “muuh” or “meh”, exit and print “you’re a loser”.
'''


if __name__ == "__main__":
    count = 0
    magic_number = int(input('Please, Choose and write the magic number: \n'))
 
    while True:
        count = count + 1
        users_number = input("Write the number or do like a cow if required: \n")
        if count % magic_number == 0:
            if users_number not in ["muuh", "meeh"]:
                print("A cow counts better than you, tha is why You're a loser")
                break
        elif str(magic_number) in str(count):
            if users_number not in ["muuh", "meeh"]:
                print("A cow counts better than you, tha is why You're a loser")
                break
        elif int(users_number) != count:
            print("You lost count and You're a loser now")
            break


    


