# Take input from the user until he/she gives the hidden number {Hidden number = 10} 

hidden_num = 10
g_num = int(input("Guess the number : "))
while(hidden_num != g_num):
    g_num = int(input("Your Guess was wrong Re-Enter the number : " ))

print("You have Guessed the right answer")