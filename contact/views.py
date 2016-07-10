from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        contactFormFullName = form.cleaned_data.get("fullName")
        contactFormEmail = form.cleaned_data.get("email")
        contactFormMessage = form.cleaned_data.get("message")

        subject = "Analytics Ticketing System Contact Form"
        fromEmail = settings.EMAIL_HOST_USER
        toEmail = [fromEmail]
        contactMessage = "%s: %s via %s"%(contactFormFullName, contactFormMessage, contactFormEmail)

        send_mail(subject=subject, message= contactMessage, from_email=fromEmail, recipient_list=toEmail, fail_silently=False)

    context = {
            "contactForm": form
    }

    return render(request, "contact_form.html", context)