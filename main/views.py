from django.shortcuts import render
# from vocab import quiz as q

def home(request):
    something = "banana"
    button = [1000, 1100, 1200, 1300, 1400, 1500]

    return render(request, 'home.html', {
        'dutch_word': something,
        'buttons': button,
        })