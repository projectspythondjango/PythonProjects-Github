from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

# Create your views here.
from .models import Task
from .forms import ToDoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class TaskListview(ListView):
    model=Task
    template_name='home.html'
    context_object_name='key1'
class TaskDetailview(DetailView):
    model=Task
    template_name='details.html'
    context_object_name='task'
class TaskUpdateview(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name='task'

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs=[{'pk':self.object.id}])
class TaskDeleteview(DeleteView):
    model=Task
    template_name='delete.html'
    # def get_success_url(self):
    #     return reverse('todoapp:cbvhome')
    success_url = reverse_lazy('todoapp:cbvhome')


def add(request):
    task1=Task.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority1=request.POST.get('priority','')
        date1=request.POST.get('date','')
        task=Task(name=name,priority=priority1,date=date1)
        task.save()

    return render(request,"home.html",{'key1':task1})
# def details(request):
#     task=Task.objects.all()
#     return render(request,"details.html",{'task':task})
#
def delete(request,taskid):
    task2=Task.objects.get(id=taskid)
    if request.method=="POST":
        task2.delete()
        return redirect('/')
    return render(request,"delete.html")
def update(request,id):
    task=Task.objects.get(id=id)
    form1=ToDoForm(request.POST or None,instance=task)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form1,'task':task})