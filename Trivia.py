"""
Filename: Trivia.py
Author: Chrobak, Walter>
Created: <9/11/2025>
Instructor: Holtslander
"""
score = 0
correct = 0

print("Hi wellcome to my trivia game it asks you questions")

q1 = input("What is the capital of Poland?\n").lower()
if q1 == "warsaw":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 1

print(score, correct)

q2 = input("Who is Dave Mustaine?\n").lower()
if q2 == "frontman of megadeth" or q2 == "former member of metallica":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 1

print(score, correct)

q3 = input("What band was Kirk Hammett on before Metallica?\n").lower()
if q3 == "exodus":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 1

print(score, correct)

q4 = input("What was the capital of Prussia?\n").lower()
if q4 == "königsberg" or q4 == "konigsberg":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 1

print(score, correct)

q5 = input("What was the capital of Poland before warsaw?\n").lower()
if q5 == "Kraków" or q5 == "Krakow":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 1

print(score, correct)

q5 = input("What is the capital of the US?\n").lower()
if q5 == "washington, d.c" or q5 == "washington":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 1

print(score, correct)

q5 = input("Who won World War 2?\n").lower()
if q5 == "the allies":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 1

print(score, correct)

q6 = input("Who was Iron Maidens former singer before bruce?\n").lower()
if q6 == "paul di'anno":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 1

print(score, correct)

q7 = input("Who became the lead singer on Black Sabbath after Ozzy Osborne?\n").lower()
if q7 == "ronnie james dio" or q7 == "dio":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 1

print(score, correct)

q8 = input("What band was dio on before Black sabbath?\n").lower()
if q8 == "rainbow":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 1

print(score, correct)

q9 = input("What did dio do after leaving sabbath?\n").lower()
if q9 == "Solo career":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 1

print(score, correct)

q10 = input("What is the capital of france?\n").lower()
if q10 == "Paris":
    score = score + 2
    correct = correct + 1
else:
    if score > 0:
        score = score - 1

print(score, correct)

print("Thank you for playing my game")














