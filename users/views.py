from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from store.models import Customer
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            customer = Customer.objects.create(user=user, name=name, telephone=phone, email=email)
            customer.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
