from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class QuestionIgnoredListFilter(admin.SimpleListFilter):
    """
    A filter for the Category admin page that filters by whether 
    a category has methods
    """
    # Title for the filter, shown in admin UI
    title = _('Ignored?')

    # Parameter for the filter
    parameter_name = 'ignored'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('ignored', _('Ignored')),
            ('not_ignored', _('Not Ignored')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value 
        # to decide how to filter the queryset.
        if self.value() == 'ignored':
            queryset = queryset.exclude(ignore_until__lt=timezone.now())
            return queryset
        if self.value() == 'not_ignored':
            queryset = queryset.exclude(ignore_until__gt=timezone.now())
            
            return queryset


