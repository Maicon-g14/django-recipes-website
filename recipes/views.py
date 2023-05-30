from django.shortcuts import render, HttpResponse

recipes = [
    {
        'author': 'Levy',
        'title': 'Perfectly Fried Egg',
        'directions': 'Break the egg, put in the fryer, heat until looks tasty(don\'t let it toast)',
        'date_posted': 'May 30, 2013'
    },
    {
        'author': 'Zack',
        'title': 'Unfried Fried Egg',
        'directions': 'Break the egg, put in the fryer, repent yourself then try to burn everything',
        'date_posted': 'Apr 1, 2015'
    },
    {
        'author': 'Eren',
        'title': 'Fake Fried Egg',
        'directions': 'Break the egg, put in the fryer, call the fire-fighters and then put fire on it',
        'date_posted': 'Apr 1, 2023'
    },
    {
        'author': 'Mikasa',
        'title': 'I Fried an Egg?',
        'directions': 'Break the egg, put in the fryer, tell Eren to continue',
        'date_posted': 'Apr 1, 2023'
    },
]

# Create your views here.
def home(request):
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context)

def about(request):
    return render(request, "recipes/about.html", {'title': 'About Us'})