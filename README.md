# 🎯 Number Guessing Game Using Python 🐍

A simple interactive number guessing game where users guess a randomly selected number within a defined range. 🕹️ The game gives smart feedback to help users guess efficiently and improves logical thinking. ✅

---

## 📌 Features

- Accepts a **user-defined range** for guessing.  
- Generates a **random number** within the selected range.  
- Provides feedback:  
  - 🔺 Too high  
  - 🔻 Too low  
  - ✅ Correct!  
- Calculates **maximum guesses** using a binary search approach.  
- Simple, beginner-friendly implementation in **Python** and can also be implemented in **C**.  

---

## 📝 How to Play

1. Run the game script.  
2. Enter the **lower and upper bounds** of the guessing range.  
3. Try to guess the number!  
4. The game will give hints after each guess: "Too high" or "Too low".  
5. Keep guessing until you find the correct number or run out of chances.  

**Example:**  

Guess a number between 1 and 50
Your guess: 25 → Too low
Your guess: 37 → Too low
Your guess: 43 → Too high
Your guess: 42 → Correct! 🎉


---

## ⚙️ Algorithm

1. Accept lower and upper bounds from the user.  
2. Generate a random number within the selected range.  
3. Calculate the maximum allowed guesses using the binary search formula.  
4. Loop to take user guesses:  
   - If guess > number → print "Too high"  
   - If guess < number → print "Too low"  
   - If guess == number → print "Congratulations!" and exit loop  
5. If user runs out of guesses → display correct number and "Better Luck Next Time!"  

---

## 💻 Installation & Usage

1. **Clone the repository:**  
```bash
git clone https://github.com/yourusername/number-guessing-game.git
cd number-guessing-game
python main.py

🔧 Technologies Used

Python 🐍

Random module 🎲

Optional: C programming version for learning purposes 💻

👨‍💻 Contribution

Feel free to ⭐ star the repo and contribute by submitting pull requests. Any improvements or optimizations are welcome!

📄 License

This project is open-source under the MIT License.
