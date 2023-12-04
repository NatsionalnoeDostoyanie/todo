from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
    )

    title = models.CharField(
        max_length=500,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    date_created = models.DateTimeField(auto_now_add=True, )
    date_updated = models.DateTimeField(auto_now=True, )

    STATUS_CHOICES = [
        ('done', 'Выполнено'),
        ('in_progress', 'В процессе выполнения'),
        ('postponed', 'Отложено'),
    ]
    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default='in_progress',
    )
    date_postponed = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['date_created', ]

    def __str__(self):
        return self.title

    def update_status(self, new_status, postponed_date=None):
        self.status = new_status
        self.date_postponed = postponed_date

        self.save()
