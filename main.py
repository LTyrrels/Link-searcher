import os, re, time
from colorama import Fore

with open("config.txt", 'r') as config_file:
    contenu = config_file.read()
    match = re.search(r"path:\s*(.*)", contenu)
    if match:
        repertory = match.group(1)

def chercher_lien(dossier, lien):
    fichiers_txt = [fichier for fichier in os.listdir(dossier) if fichier.endswith('.txt')]
    resultats = []

    for fichier in fichiers_txt:
        chemin = os.path.join(dossier, fichier)
        with open(chemin, 'r', encoding='utf-8') as f:
            lignes = f.readlines()
            for ligne in lignes:
                if lien in ligne:
                    resultats.append(ligne.strip())

    return resultats

def enregistrer_resultats(resultats, lien):
    with open(f'output/{lien}.txt', 'w', encoding='utf-8') as f:
        for resultat in resultats:
            f.write(resultat + '\n')



print(f"> Made by {Fore.RED}@jamy667{Fore.RESET} on telegram")

lien = input("> Entrez le lien : ")
start_time = time.time()
resultats = chercher_lien(repertory, lien)
end_time = time.time()
time_elapsed = end_time - start_time
number_file = sum(1 for fichier in os.listdir(repertory) if fichier.endswith('.txt'))
enregistrer_resultats(resultats, lien)

with open(f"{lien}.txt", 'r', encoding='utf-8') as output_file:
    account_number = len(output_file.readlines())

print(f"> Files found in the path: {number_file}")
print(f"> Time elapsed : {time_elapsed} seconds")
print(f"> Number of account found for {lien}: {account_number}")
