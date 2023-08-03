import pandas as pd

base = pd.read_excel("base.xlsx")
tmplt = pd.read_excel("template.xlsx")
note = pd.read_excel("note.xlsx")

fix = 0 #pour maintenir la ligne a ajouter

for etudiant in range(int(base["nombre_etudiant"][0])) : #boucle principale sur le nombre d'etudiants
    for question in range(int(base["nombre_question"][0])) : #boucle sur le nombre de questions
        tmplt.at[fix, "utilisateur"] = base["nom"][etudiant] #pour eviter une tentative d'accès à une adresse non assignée
        tmplt["ecole"][fix] = base["ecole"][0]
        tmplt["langue"][fix] = base["langue"][0]
        tmplt["annees"][fix] = base["annee"][0]
        tmplt["session"][fix] = base["session"][0]
        tmplt["competence"][fix] = base["competence"][0]
        tmplt["diplome"][fix] = base["diplome"][question]
        tmplt["question_type"][fix] = base["question_type"][question]
        tmplt["question_numero"][fix] = question + 1
        tmplt["support"][fix] = base["support"][0]
        tmplt["enonce"][fix] = base["enonce"][question]
        tmplt["reponse_referente"][fix] = base["reponse_referente"][question]
        tmplt["reponse_referente"][fix] = base["reponse_referente"][question]
        tmplt["note_sur"][fix] = base["note_sur"][question]
        tmplt["note"][fix] = note[f"Q{question+1}"][etudiant]
        tmplt["note_sur_10"][fix] = round((note[f"Q{question+1}"][etudiant] * 10) / base["note_sur"][question], 2)
        tmplt.to_excel("tmplt.xlsx", index=False) #pour prendre en compte les modifications
        fix += 1
    tmplt.at[fix, "utilisateur"] = " " #ajouter une ligne vide
    tmplt.to_excel("tmplt.xlsx", index=False)
    fix += 1

print(tmplt)
print(base)