from django.contrib import admin
from .models import Etudiant, Question, Note

# Register your models here.
admin.site.register(Etudiant)
admin.site.register(Question)
admin.site.register(Note)