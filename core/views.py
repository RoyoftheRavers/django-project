from django.shortcuts import render, redirect
from .models import Contact

def home(request):
    context = {
        'site_name': 'My Website',
        'tagline': 'A place for football, music, and everything Dublin.',
        'features': [
            {'title': 'Football', 'description': 'Bohemian FC, Manchester United, and the beautiful game from a Dublin perspective.'},
            {'title': 'Music', 'description': 'Exploring tech house, its roots, its artists, and the best nights Dublin has to offer.'},
            {'title': 'Dublin Life', 'description': 'GAA, culture, and everything that makes Dublin one of Europe\'s great cities.'},
        ]
    }
    return render(request, 'core/home.html', context)

def about(request):
    context = {
        'site_name': 'My Website',
    }
    return render(request, 'core/about.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print('POST data:', request.POST)
        print('name:', name)
        print('email:', email)
        print('subject:', subject)
        print('message:', message)

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect('contact_success')

    return render(request, 'core/contact.html')

def contact_success(request):
    return render(request, 'core/contact_success.html')