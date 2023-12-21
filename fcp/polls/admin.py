from django.contrib import admin
from .models import Question, Choice

# Register your models here.

admin.site.site_header = 'The poll mall'
admin.site.site_title = 'voting admin area'
admin.site.index_title = 'welcome to our admin voting area'



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': 
                  ['collapse']}),]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)