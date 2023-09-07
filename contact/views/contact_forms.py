from django.shortcuts import render, redirect
from contact.forms import ContactForms


def create(request):
    form = ContactForms()

    if request.method == 'POST':
        form = ContactForms(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contact:create')

    context = {
        'form': form
    }

    return render(request, 'contact/create.html', context)
