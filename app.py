import os
from openai import AzureOpenAI
from dotenv import load_dotenv
import gradio as gr

#Chargement des variables d'environnement depuis le fichier .env
load_dotenv()
api_version = os.getenv("api_version")
subscription_key = os.getenv("api_key")
endpoint = os.getenv("endpoint")
deployment_name = os.getenv("deployment_name")

# Initialisation du client Azure OpenAI
client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

#Fonction de chat pour envoyer le message de l'utilisateur au model-router et obtenir une réponse
def chat(user_message, history):

    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

 # Ajouter l'historique de la conversation
    for msg in history:
        messages.append({"role": msg["role"], "content": msg["content"]})

    # Ajouter le nouveau message de l'utilisateur
    messages.append({"role": "user", "content": user_message})

    # Appeler l'API Foundry
    response = client.chat.completions.create(
        messages=messages,
        max_tokens=8192,
        temperature=0.7,
        top_p=0.95,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        model=deployment_name
    )

    # Afficher le modèle choisi par le routeur dans la console
    print("Model chosen by the router:", response.model)
    print("Nbr total de tokens consommés", response.usage.total_tokens )
    return response.choices[0].message.content

# Construction de l'interface graphique avec Gradio ChatInterface
foundry_model_router_chatbot = gr.ChatInterface(
    fn=chat,
    title="🤖 ModelRouter Chatbot",
    description="Assistant IA propulsé par Model Router avec MS Foundry",
)

# Lancement de l'interface
if __name__ == "__main__":
    foundry_model_router_chatbot.launch(theme=gr.themes.Citrus())








#WORKING CODE

# response = client.chat.completions.create(
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful assistant.",
#         },
#         {
#             "role": "user",
#             "content": "Agis comme un comité d’experts pluridisciplinaires. Examine un scénario hypothétique où une IA autonome prend des décisions ayant des impacts humains irréversibles. Tâches :- formuler plusieurs cadres d’interprétation possibles du scénario- analyser les tensions entre efficacité, responsabilité et justice- expliciter les hypothèses implicites derrière chaque position- discuter les limites, incertitudes et zones grises- proposer des principes de gouvernance plutôt que des solutions finales. Contraintes :- raisonnement nuancé et non conclusif- positions contradictoires présentées équitablement- explicitation des limites du raisonnement- structure claire avec sections- minimum 1000 mots- ton prudent et réflexif",
#         }
#     ],
#     max_tokens=8192,
#     temperature=0.7,
#     top_p=0.95,
#     frequency_penalty=0.0,
#     presence_penalty=0.0,
#     model=deployment_name
# )

# print("Model chosen by the router: ", response.model)
# print(response.choices[0].message.content)

