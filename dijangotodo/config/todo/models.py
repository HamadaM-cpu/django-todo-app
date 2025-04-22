from django.db import models
from django.utils import timezone

class Todo(models.Model):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    PRIORITY_CHOICES = [
        (LOW, '低'),
        (MEDIUM, '中'),
        (HIGH, '高'),
    ]

    title = models.CharField("タスク名", max_length=30)
    description = models.TextField("詳細", blank=True)
    deadline = models.DateField("締切")
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)  # 作成日時
    updated_at = models.DateTimeField(auto_now=True)  # 更新日時

    def __str__(self):
        return self.title
