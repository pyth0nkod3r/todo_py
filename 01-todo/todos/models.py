from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # This helps Django redirect after a successful Create/Update
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('todo-list')