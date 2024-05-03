from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import EmployeeForm
# Create your views here.
'''@login_required
def home(request):
    return render(request,'home.html',{})'''

class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return render(self.request,self.template_name,{'form':form})
    
def home(request):
    return render(request,'accounts/home.html') 

def index(request):
    return render(request,'accounts/index.html')   
    
def logout_view(request):
    logout(request)
    return redirect('login') 

@login_required
def add_employee(request):
    if request.method == 'POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user
            employee.save()
            return HttpResponse('Registration successful !')
    else:
        form = EmployeeForm()
    return render(request,'employee/add.html',{'form':form})           