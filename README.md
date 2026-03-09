# 🤖 ModelRouter Chatbot

Assistant IA conversationnel propulsé par **AI Foundry Model Router** avec une interface web Gradio.

## 📋 Description

Cette application est un chatbot intelligent qui utilise le **Model Router** de Microsoft Foundry pour router automatiquement les requêtes vers le modèle LLM le plus adapté. Le routeur sélectionne dynamiquement le meilleur modèle en fonction du contexte et de la complexité de la conversation.

### Fonctionnalités

- 💬 Interface de chat intuitive avec Gradio
- 🔄 Historique de conversation persistant
- 🎯 Routage intelligent vers le modèle optimal (via Model Router)
- 📊 Affichage du modèle choisi et des tokens consommés dans la console

## 🚀 Installation

### Prérequis

- Python 3.10+
- Un compte Azure avec accès à Azure AI Foundry
- Un déploiement Model Router configuré

### Étapes

1. **Cloner le repo**
   ```bash
   git clone https://github.com/fchambon/ai-foundry-modelrouter-app.git
   cd ai-foundry-modelrouter-app
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # ou
   source .venv/bin/activate  # Linux/macOS
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer les variables d'environnement**
   
   Créer un fichier `.env` à la racine du projet :
   ```env
   api_version=2024-12-01-preview
   api_key=<votre-clé-api>
   endpoint=<votre-endpoint-foundry>
   deployment_name=<nom-du-deployment-model-router>
   ```

## ▶️ Utilisation

Lancer l'application :

```bash
python app.py
```

L'interface web s'ouvre automatiquement dans votre navigateur (par défaut : `http://127.0.0.1:7860`).

## 🏗️ Architecture

```
App/
├── app.py              # Application principale
├── requirements.txt    # Dépendances Python
├── .env               # Variables d'environnement (non versionné)
├── .gitignore         # Fichiers exclus de Git
└── README.md          # Documentation
```

## 🔧 Technologies

- **[Azure OpenAI SDK](https://pypi.org/project/openai/)** - Client pour Azure AI Foundry
- **[Gradio](https://gradio.app/)** - Interface web interactive
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** - Gestion des variables d'environnement

## 📝 Notes

- Le Model Router affiche dans la console le modèle sélectionné pour chaque requête
- Les tokens consommés sont également loggés pour le suivi des coûts

## 📄 Licence

MIT