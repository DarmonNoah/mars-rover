import os
import re

# Chemin du projet à analyser
base_path = "C:/Users/Titi/mars-rover/CSharp xUnit starter"

# Récupération des fichiers .cs
cs_files = []
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".cs"):
            cs_files.append(os.path.join(root, file))

# Analyse de chaque fichier
for f in cs_files:
    print(f"\n--- Analyse du fichier : {os.path.basename(f)} ---")
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

        # 1. Usings : dépendances techniques
        usings = re.findall(r'using\s+([\w\.]+);', content)

        # 2. Instanciations : dépendances directes via new
        instanciations = re.findall(r'new\s+(\w+)\s*\(', content)

        # 3. Appels statiques : Classe.Methode()
        static_calls = re.findall(r'(\w+)\.\w+\(', content)

        print(f"Usings trouvés : {set(usings)}")
        print(f"Instanciations trouvées : {set(instanciations)}")
        print(f"Appels statiques trouvés : {set(static_calls)}")
        