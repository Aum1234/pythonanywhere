from django.contrib import admin

from .models import Question, Choice , TakatafoodType , Takatafood

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(TakatafoodType)
admin.site.register(Takatafood)