from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

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
    return render(request, 'core/about.html', {'site_name': 'My Website'})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'core/contact_success.html')

@login_required
def profile(request):
    context = {
        'user': request.user,
    }
    return render(request, 'core/profile.html', context)