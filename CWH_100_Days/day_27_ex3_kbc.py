# Create a program capable of displaying questions to the user like KBC. 
# Use List data type to store the questions and their correct answers. 
# Display the final amount the person is taking home after playing the game.

ques = [
    ["Which planet is known as the Red Planet?",
     "Earth",
     "Mars",
     "Jupiter",
     "Venus"],

    ["How many days are there in a leap year?",
     "365",
     "364",
     "366",
     "367"],

    ["Which of these is the largest continent by area?",
     "Africa",
     "Asia",
     "Europe",
     "North America"],

    ["Which language is primarily used to style web pages?",
     "Python",
     "HTML",
     "CSS",
     "SQL"],

    ["Which is the largest ocean on Earth?",
     "Atlantic Ocean",
     "Indian Ocean",
     "Arctic Ocean",
     "Pacific Ocean"],

    ["Who was the first person to walk on the Moon?",
     "Yuri Gagarin",
     "Neil Armstrong",
     "Buzz Aldrin",
     "Michael Collins"],

    ["Which element has the chemical symbol Fe?",
     "Fluorine",
     "Iron",
     "Fermium",
     "Francium"],

    ["Which Indian city is popularly known as the Silicon Valley of India?",
     "Hyderabad",
     "Pune",
     "Bengaluru",
     "Chennai"],

    ["What does CPU stand for in computing?",
     "Central Processing Unit",
     "Computer Processing Utility",
     "Central Program Unit",
     "Core Processing Utility"],

    ["Which of these is NOT a programming language?",
     "Python",
     "Java",
     "HTML",
     "C++"],

    ["Which fundamental force keeps planets in orbit around the Sun?",
     "Electromagnetic force",
     "Strong nuclear force",
     "Gravity",
     "Weak nuclear force"],

    ["Which Indian mission successfully landed near the Moon's south polar region in 2023?",
     "Chandrayaan-1",
     "Chandrayaan-2",
     "Chandrayaan-3",
     "Mangalyaan"],

    ["In the binary number system, what is the decimal value of 1010?",
     "8",
     "10",
     "12",
     "14"],

    ["Which data structure follows the LIFO principle?",
     "Queue",
     "Stack",
     "Linked List",
     "Tree"],

    ["Which of these sorting algorithms has an average-case time complexity of O(n log n)?",
     "Bubble Sort",
     "Selection Sort",
     "Merge Sort",
     "Linear Search"],

    ["Which theorem states that in a right-angled triangle, the square of the hypotenuse equals the sum of the squares of the other two sides?",
     "Euclid's theorem",
     "Pythagorean theorem",
     "Binomial theorem",
     "Fermat's theorem"]
]

ans = ["B","C","B","C","D","B","B","C","A","C","C","C","B","B","C","B"]

prize = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 7500000, 10000000]

confirmed_prize = 0
for i in range(0, len(ques)):
    print("Q",i+1,".", ques[i][0])
    print("A.", ques[i][1])
    print("B.", ques[i][2])
    print("C.", ques[i][3])
    print("D.", ques[i][4])

    user_answer = input("Enter your answer: ")
    
    correct_answer = ans[i]

    if user_answer == correct_answer:
        print(prize[i], "rupees won!!!")
        if i>=0 and i<=3:
            confirmed_prize = 0
        elif i>=4 and i<=8:
            confirmed_prize = 10000
        elif i>=9 and i<=15:
            confirmed_prize = 320000
            if i == len(ques) - 1:
                print("Congratulations! You won", prize[i], "rupees")
    else:
        print("wrong answer")
        print("you win", confirmed_prize, "rupees")
        break








