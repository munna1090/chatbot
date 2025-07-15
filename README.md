# Student Mentor Chatbot 🚀

This is a Flask-based chatbot deployed to Google Cloud Run.

**Live URL:** [https://chatbot-804194266797.us-central1.run.app/](https://chatbot-804194266797.us-central1.run.app/)

## Tech Stack
- Python 3
- Flask
- Vertex AI GenAI (Gemini)
- Cloud Run (Serverless)

## Deploy

1. Build:
    ```bash
    gcloud builds submit --tag gcr.io/PROJECT_ID/chatbot
    ```

2. Deploy:
    ```bash
    gcloud run deploy chatbot --image gcr.io/PROJECT_ID/chatbot --platform managed --region us-central1 --allow-unauthenticated
    ```

## Note
**DO NOT** commit your service account JSON key!
