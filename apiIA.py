
import requests
import json

url = "http://localhost:11434/api/generate"
headers = {'Content-Type': 'application/json'}

def toAI(sujet):
    data = {
    "model": "mistral",
    "prompt": f'''
À partir du texte suivant, rédigez un poste linkedin reprenant le sujet concis et professionnel adapté à un post LinkedIn :
{sujet}
Le résumé doit capter les points essentiels du sujet et présenter une vue d'ensemble claire et engageante pour un public professionnel, rajoute des emojis.
'''

}

    response = requests.post(url, headers=headers, data=json.dumps(data))
    textGenerated = ""
    try:
        # Séparation des objets JSON par des sauts de ligne
        parts = response.text.split('\n')

        # Parcours de chaque partie pour la parser et la traiter individuellement
        for part in parts:
            if part.strip():  # Vérifie que la partie n'est pas vide
                json_data = json.loads(part)
                textGenerated +=json_data["response"]

        return textGenerated
    except json.JSONDecodeError:
        return ("Erreur de décodage JSON : vérifiez la réponse du serveur.")

