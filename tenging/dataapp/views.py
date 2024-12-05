from django.shortcuts import render, redirect
from .models import Notendur
from .forms import NotendurForm

def create(request):
    if request.method == 'POST':
        form = NotendurForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new Notendur instance
            return redirect('index')  # Redirect after saving
    else:
        form = NotendurForm()  # Empty form for creating a new entry

    return render(request, 'dataapp/update.html', {'form': form})
