from question_model import Question
from data import question_data


question_bank = []

for i in range(len(question_data)):
    q = ""
    a = ""
    for key, value in question_data[i]:
        q = key
        a = value
        print(f"question: {q} ||| answer: {a}")
