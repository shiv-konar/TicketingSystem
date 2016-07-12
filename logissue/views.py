from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import IssueLogForm, AddMessageForm
from .models import IssueLog, AddMessage

def issuelog(request):
    form = IssueLogForm(request.POST or None)
    context = {
        "form" : form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.issued_by = request.user
        instance.save()

        issueFormUser = request.user

        subject = "New Issue Logged"
        fromEmail = settings.EMAIL_HOST_USER
        toEmail = ["shiv.konar@ogilvy.com"]
        contactMessage = "New Issue Logged by %s" % (issueFormUser)

        send_mail(subject=subject, message=contactMessage, from_email=fromEmail, recipient_list=toEmail,
                  fail_silently=False)
    return render(request, "logissue.html", context)

def administration(request):
    issues_list = IssueLog.objects.order_by("-issued_on")

    form = AddMessageForm(request.POST or None)
    context = {
        "form":form,
        "issues_list":issues_list,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.issue_description_id = issues_list.objects.get(pk)
        instance.save()

        issueFormUser = request.user

        subject = "Additional message added"
        fromEmail = settings.EMAIL_HOST_USER
        toEmail = ["shiv.konar@ogilvy.com"]
        contactMessage = "New message added by %s" % (issueFormUser)

        send_mail(subject=subject, message=contactMessage, from_email=fromEmail, recipient_list=toEmail,
                  fail_silently=False)
    return render(request, "administration.html", context)