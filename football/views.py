from django.shortcuts import render

def football_home(request):
    context = {
        'title': 'Football',
        'subtitle': 'Live data coming soon — powered by Django.',
    }
    return render(request, 'football/home.html', context)
