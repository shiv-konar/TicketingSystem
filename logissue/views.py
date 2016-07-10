from django.shortcuts import render
from .forms import IssueForm

# Create your views here.


def logissue(request):
    form = IssueForm(request.POST or None)
    context = {
        "logIssueform" : form
    }

    return render(request, 'logissue.html', context)