from django.shortcuts import render
from contact.forms import ContactForms


def create(request):
    form = ContactForms()

    if request.method == 'POST':
        form = ContactForms(request.POST)

    context = {
        'form': form
    }

    return render(request, 'contact/create.html', context)
