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

