from django.shortcuts import render
from .models import Word
import random

def question(request):
    quiz = generateQuestion()

    dutchWord = quiz[0]
    correctAnswer = quiz[1]
    wrongAnswers = quiz[2]

    answerOptions = [correctAnswer] + wrongAnswers

    random.shuffle(answerOptions)

    return render(request, 'main/index.html', {
        'dutchWord': dutchWord,
        'buttons': answerOptions,
        })

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
