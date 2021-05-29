from django.shortcuts import render
# from vocab import quiz as q

def home(request):
    something = "banana"
    example = 1 + 1

    return render(request, 'home.html', {
        'dutch_word': something,
        'button1': example,
        'button2': example,
        'button3': example,
        'button4': example,
        'button5': example,
        'button6': example,
        })