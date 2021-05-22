from dateutil.relativedelta import relativedelta

from django.utils.safestring import mark_safe
from django.db import models
from django.utils import timezone
from django.utils.html import strip_tags

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Question(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        help_text="Category this question belongs to"
    )
    question = RichTextUploadingField()
    answer = RichTextUploadingField()
    ignore_until = models.DateTimeField(
        null=True,
        blank=True,
    )
    hide_indefinitely = models.BooleanField(
        blank=False,
        null=False,
        default=False,
    )

    def __str__(self):
        if self.hide_indefinitely:
            string = "(Question hidden indefinitely)"
        elif self.ignore_until > timezone.now():
            print(self.ignore_until, timezone.now())
            tdelta = relativedelta(self.ignore_until, timezone.now())
            string = f'(Ignoring for {tdelta.days} days, {tdelta.hours} hours)'
        else:
            string = ''
        return f'({self.category.name}): {strip_tags(self.question)} {string}'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.ignore_until = timezone.now()
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(
        max_length=127,
        blank=False,
        unique=True,
        help_text="Name for category"
    )

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'

