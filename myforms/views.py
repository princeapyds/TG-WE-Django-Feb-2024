from django.shortcuts import render, HttpResponseRedirect
from .forms import MyForm

def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('../success/')
    else:
        form = MyForm()
    return render(request, 'myforms/my_template.html', {'form': form})


def success_view(request):
    return render(request, 'myforms/success.html')
