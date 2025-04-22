from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo

class TodoList(ListView):
    model = Todo
    context_object_name = "tasks"
    template_name = "todo/todo_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("search")
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

class TodoToggle(View):
    def get(self, request, pk):
        task = get_object_or_404(Todo, pk=pk)
        task.completed = not task.completed  # 完了・未完了を切り替え
        task.save()
        return redirect('list')  # リストに戻る

class TodoCreate(CreateView):
    model = Todo
    fields = ["title", "description", "deadline"]
    success_url = reverse_lazy("list")

class TodoUpdate(UpdateView):
    model = Todo
    fields = ["title", "description", "deadline"]
    success_url = reverse_lazy("list")

class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("list")

class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"
    template_name = "todo/todo_detail.html"
