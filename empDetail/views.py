from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Employee
from django.views.generic import ListView,CreateView,DeleteView,DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Create your views here.

class EmployeeList(ListView):
    model = Employee
    template_name = 'empDetail/home.html'
    context_object_name = 'employees'
    ordering = ['-joining_date']
    paginate_by = 4

    def get_queryset(self):
        search = self.request.GET.get("search")
        if search:
            object_list = self.model.objects.filter(
                Q(first_name__icontains = search) |
                Q(last_name__icontains = search) |
                Q(description__icontains = search)
            )
        else:
            object_list = self.model.objects.all()

        return object_list

class EmployeeCreate(LoginRequiredMixin,CreateView):
    model = Employee
    fields = ['first_name','last_name','description']

    def form_valid(self,form):
        form.instance.employer = User.objects.first()
        return super().form_valid(form)

class EmployeeDetailView(DetailView):
    model = Employee

class EmployeeDeleteView(LoginRequiredMixin,DeleteView):
    model = Employee
    success_url = '/'

    def test_func(self):
        employee = self.get_object()
        if self.request.user == employee.employer:
            return True
        return False

class EmployeeUpdateView(LoginRequiredMixin,UpdateView):
    model = Employee
    fields = ['description']
    template_name='empDetail/employee_update_form.html'

    def form_valid(self,form):
        form.instance.employer = User.objects.first()
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author :
    #         return True
    #     return False