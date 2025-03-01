from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
# If there are many fields, manage fields as a set.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["question_txt"]}),
        ("Date information", {"fields":["pub_date"], "classes":["collapse"]}),
        ]
    inlines = [ChoiceInline]
    list_display = ["question_txt", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_txt"]

admin.site.register(Question, QuestionAdmin)

