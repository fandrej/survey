from django.contrib import admin
from . models import *

# Register your models here.
class QuestionsInline(admin.TabularInline):
    model = Questions
    verbose_name_plural = "Poll questions"
    fields = ['question_type', 'question_text', 'answer', ]
    ordering = ('id', )
    #fk_name = "busversion"
    extra = 0   # remopve last empty rows

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    verbose_name_plural = "Polls"
    list_display = ('id', 'name', 'date_start', 'date_end')
    readonly_fields = [('date_start')]
    search_fields = ['name']
    date_hierarchy = 'date_start'
    inlines = [QuestionsInline]

    def get_queryset(self, request):
        qs = super(PollAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return None
