from django.shortcuts import render, redirect
import random

# Create a site that allows a user to play this guessing game. Upon loading, the server should "pick" a random number between 1-100; store the number in session. Allow the user to guess the number--tell them when they are too high or too low. If they guess the correct number, notify them and offer to play again.

# There are many different ways to do this assignment. When you finish the basic functionality, find a peer and compare your code!

def index(request):
    if "num" not in request.session:
        request.session["num"] = random.randint(1, 100)
    print(request.session["num"])
    return render(request, 'index.html')

def guess(request):
    request.session['userGuess'] = int(request.POST['userInput'])
    return redirect("/")

def reset(request):
    request.session.pop("num")
    return redirect("/")