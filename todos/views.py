# todos/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404

from todo_py.todos.forms import TodoForm
from .models import Todo

# 1. List all TODOs
class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'
    
    # Order by unresolved first, then by due date
    def get_queryset(self):
        return Todo.objects.order_by('is_resolved', 'due_date')

# 2. Create a new TODO
class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_form.html'

# 3. Edit a TODO
class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_form.html'

# 4. Delete a TODO
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todos/todo_confirm_delete.html'
    success_url = reverse_lazy('todo-list')

# 5. Custom View: Quick Toggle "Resolved"
def toggle_todo_status(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_resolved = not todo.is_resolved
    todo.save()
    return redirect('todo-list')