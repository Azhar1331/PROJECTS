quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "What is the Square of 12'?",
        "options": ["A. 4", "B. 9", "C. 144", "D. 121"],
        "answer": "C"
    },
    {
        "question": "Which one of the following is not a linear data structure?",
        "options": ["A. Array", "B. Linked List", "C. Tree"],
        "answer": "C"
    },
    {
        "question": "Which one of the following is not a linear data structure?",
        "options": ["A. Array", "B. Linked List", "C. Tree"],
        "answer": "C"
    },
    {
        "question": "Which one of the following is not a linear data structure?",
        "options": ["A. Array", "B. Linked List", "C. Tree"],
        "answer": "C"
    },
    {
        "question": "Which one of the following is not a linear data structure?",
        "options": ["A. Array", "B. Linked List", "C. Tree"],
        "answer": "C"
    },
    {
        "question": "Which one of the following is not a linear data structure?",
        "options": ["A. Array", "B. Linked List", "C. Tree"],
        "answer": "C"
    },
    {
        "question": "Which one of the following is not a linear data structure?",
        "options": ["A. Array", "B. Linked List", "C. Tree"],
        "answer": "C"
    },
    {
        "question": "Which one of the following is not a linear data structure?",
        "options": ["A. Array", "B. Linked List", "C. Tree"],
        "answer": "C"
    },
    {
        "question": "Which one of the following is not a linear data structure?",
        "options": ["A. Array", "B. Linked List", "C. Tree"],
        "answer": "C"
    },
] 

def run_quiz(questions):
    score = 0
    #Loop through each question dictionary  in the list
    for q in questions:
        print("\n" + "="*30)
        print(q["question"])
        
        #Loop Through the options and Display
        for option in q["options"]:
            print(option)
            
        user_answer = input("Enter your options (A , B , C , D) : ").upper()    
        
        if user_answer == q["answer"]:
            print("Correct Answer")
            score += 1
        else:
            print(f"Incorrect , The answer is {q['answer']} ")    

    # Display final score
    print("\n" + "="*30)
    print("✨ Quiz Finished! ✨")
    print(f"You scored {score} out of {len(quiz_questions)}.")            



run_quiz(quiz_questions)           