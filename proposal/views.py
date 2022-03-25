from django.shortcuts import render, redirect

# Create your views here.
from .models import proposal
from .forms import SubmitProposalForm


def submit_proposal(request):
    user = request.user
    if request.method == 'POST':
        form = SubmitProposalForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.author = request.user
            p.save()
            return redirect('/')
    else:
        form = SubmitProposalForm()

    return render(request, 'newproposal.html', {'form': form, })
