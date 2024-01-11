quiz = {
    "question1": {
        "question": "Ce capitală europeană se află în Franța?",
        "answer": "Paris"
    },
    "question2": {
        "question": "Care este capitala Germaniei?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "Care este capitala Italiei?",
        "answer": "Roma"
    },
    "question4": {
        "question": "Ce capitală europeană se află în Spania?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "Care este capitala Portugaliei?",
        "answer": "Lisabona"
    },
    "question6": {
        "question": "Ce capitală europeană se află în Elveția?",
        "answer": "Bern"
    },
    "question7": {
        "question": "Care este capitala Austriei?",
        "answer": "Viena"
    },
    "question8": {
        "question": "Care este capitala Olandei?",
        "answer": "Amsterdam"
    },
    "question9": {
        "question": "Ce capitală europeană se află în Belgia?",
        "answer": "Bruxelles"
    },
    "question10": {
        "question": "Care este capitala Suediei?",
        "answer": "Stockholm"
    },
}


def run_quiz(quiz: dict):
    score = 0
    for key, value in quiz.items():
        print(value['question'])
        answer = input("Introdu raspuns:")
        if answer.lower() == value['answer'].lower():
            print("Correct!")
            score += 1
            print(f"Scorul tau este : {score}")
            print("")
            print("")
        else:
            print("Raspuns gresit")
            print(f"Raspunsul corect este : {value['answer']}")
            print(f"Scorul tau este : {score}")
            print("")
            print("")

    print(f"Ai Raspuns corect la {score} intrebari din 10 ! Felicitari!")


run_quiz(quiz)
