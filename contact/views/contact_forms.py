from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForms
from django.urls import reverse
from contact.models import Contact


def create(request):
    form = ContactForms()
    form_url = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForms(request.POST)

        if form.is_valid():
            contact_form = form.save()
            return redirect('contact:update', contact_id=contact_form.pk)

    context = {
        'form': form,
        'form_url': form_url
    }

    return render(request, 'contact/create.html', context)


def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_url = reverse('contact:update', args=(contact_id,))
    form = ContactForms(instance=contact)

    if request.method == 'POST':
        form = ContactForms(request.POST, instance=contact)

        if form.is_valid():
            contact_form = form.save()
            return redirect('contact:update', contact_id=contact_form.pk)

    context = {
        'form': form,
        'form_url': form_url
    }

    return render(request, 'contact/create.html', context)


def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        context={
            'contact': contact,
            'confirmation': confirmation
        }
    )
