import datetime
from django.shortcuts import render

context_dict = [
    {'name': 'John Doe', 'age': 28, 'profession': 'Engineer', 'visited': datetime.datetime.now()},
    {'name': 'Alice Smith', 'age': 35, 'profession': 'Teacher', 'visited': datetime.datetime.now()},
    {'name': 'Bob Johnson', 'age': 42, 'profession': 'Doctor', 'visited': datetime.datetime.now()},
    {'name': 'Eve Williams', 'age': 30, 'profession': 'Artist', 'visited': datetime.datetime.now()},
    {'name': 'Charlie Brown', 'age': 38,
        'profession': 'Lawyer', 'visited': datetime.datetime.now()},
    {'name': 'Grace Davis', 'age': 45,
        'profession': 'Scientist', 'visited': datetime.datetime.now()},
    {'name': 'David Taylor', 'age': 32, 'profession': 'Writer', 'visited': datetime.datetime.now()},
    {'name': 'Sophie Clark', 'age': 29,
        'profession': 'Entrepreneur', 'visited': datetime.datetime.now()},
    {'name': 'Frank White', 'age': 36, 'profession': 'Chef', 'visited': datetime.datetime.now()},
    {'name': 'Olivia Miller', 'age': 40,
        'profession': 'Architect', 'visited': datetime.datetime.now()}
]


def index(request):
    return render(request, 'index.html', {'context_dict': context_dict})
