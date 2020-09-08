"""Front page views."""

import random

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Quotation
from .forms import QuotationForm

#from privacytracker.models import Company

def index(request):
    """The landing page view."""

    #just_a_few = Company.objects.get_queryset().all()
    #sample = [just_a_few[0],]

    return render(request, "frontpage/index.html", {"title": "Cybersecurity, privacy, reverse engineering",})
                                                    #"sample": sample})

def contact(request):
    """The view for the contact page."""

    list_of_quotes = Quotation.objects.get_queryset().order_by('pk')

    if list_of_quotes:
        random_quote = random.choice(list_of_quotes)

        return render(request, "frontpage/contact.html", {"title": "Contact",
                                                        "random_quote": random_quote})

    return render(request, "frontpage/contact.html", {"title": "Contact",})

def privacypolicy(request):
    """The view for the privacy policy page."""
    return render(request, "frontpage/privacypolicy.html", {"title": "Privacy Policy"})

def termsofuse(request):
    """The view for the terms of use page."""
    return render(request, "frontpage/termsofuse.html", {"title": "Terms of Use"})

@login_required
def quote(request):
    """The view for the adding quote page."""
    if request.method == "POST":
        form = QuotationForm(request.POST)
        if form.is_valid():
            a_quote = form.save(commit=False)

            a_quote.save()
            return redirect('.', pk=Quotation.pk)
    else:
        form = QuotationForm()

    return render(request, "frontpage/quote.html", {"title": "Add a quote", "form": form})
