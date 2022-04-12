from tkinter import Button
from django.shortcuts import render
from .models import Word
import random

def index(request):
    return render(request, 'quiz/index.html')

def milionere(request):
    quiz = generateQuestion()

    dutchWord = quiz[0]
    answerCorrect = quiz[1]
    answerWrong = quiz[2]

    answerOptions = [answerCorrect] + answerWrong

    random.shuffle(answerOptions)

    context = {
        'dutchWord': dutchWord,
        'buttons': answerOptions,
        }
    print(answerOptions[0])
    return render(request, 'quiz/milionere.html', context)

def answer(request):
    return render(request, 'main/answer.html')

def generateQuestion():
    words = list(Word.objects.all())
    random.shuffle(words)
    question = words[0].polish
    correctAnswer = words[0].dutch
    words.pop(0)
    wrongAnswers = []

    wrong = random.sample(words, 3)
    for w in wrong:
        wrongAnswers.append(w.dutch)

    return question, correctAnswer, wrongAnswers