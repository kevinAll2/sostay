import pandas as pd
from django.shortcuts import render
from .models import Etudiant, Question, Note
  
def dashboard(request):
    base = pd.read_excel("base.xlsx")
    note = pd.read_excel("note.xlsx")

    data = []

    for etudiant in range(int(base["nombre_etudiant"][0])):
        for question in range(int(base["nombre_question"][0])):
            # Créer ou mettre à jour les objets Django pour les étudiants, questions et notes
            etudiant_obj, _ = Etudiant.objects.get_or_create(nom=base["nom"][etudiant], ecole=base["ecole"][0], langue=base["langue"][0])
            question_obj, _ = Question.objects.get_or_create(diplome=base["diplome"][question], question_type=base["question_type"][question])
            note_obj, _ = Note.objects.get_or_create(etudiant=etudiant_obj, question=question_obj, note=note[f"Q{question+1}"][etudiant])
            
            data.append({
                "etudiant": etudiant_obj,
                "question": question_obj,
                "note": note_obj.note,
                "note_sur_10": round((note_obj.note * 10) / question_obj.note_sur, 2)
            })

    context = {
        "data": data
    }

    return render(request, 'dashboard.html', context)
