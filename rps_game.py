import random
choices = ["🪨 Rock", "📄 Paper", "✂ Scissors"]
user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_choice >= 3 or user_choice < 0:
    print("❌ You entered an invalid number. You lose.")
else:
    comp_choice = random.randint(0, 2)
    
    print("\n🧍 You chose:", choices[user_choice])
    print("💻 Computer chose:", choices[comp_choice])

    if user_choice == comp_choice:
        print("🤝 It's a draw!")
    elif (user_choice == 0 and comp_choice == 2) or \
         (user_choice == 1 and comp_choice == 0) or \
         (user_choice == 2 and comp_choice == 1):
        print("🎉 You win!")
    else:
        print("😔 You lose!")
