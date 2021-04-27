from django.db import models

# Create your models here.
class Question(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        help_text="Category this question belongs to"
    )
    question = models.TextField(
        max_length=2000,
        blank=False,
        help_text="The question"
    )
    answer = models.TextField(
        max_length=2000,
        blank=False,
        help_text="Answer to the question"
    )
    ignore_until = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f' ({self.category.name}): {self.question}'

class Category(models.Model):
    name = models.CharField(
        max_length=127,
        blank=False,
        unique=True,
        help_text="Name for category"
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'Category: {self.name}'