# Mon API FastAPI

Une API simple créée avec FastAPI.

## Installation

1. Clonez le repository
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Lancement de l'application

```bash
uvicorn app.main:app --reload
```

L'API sera accessible à l'adresse : http://localhost:8000

## Documentation automatique

- Swagger UI : http://localhost:8000/docs
- ReDoc : http://localhost:8000/redoc

## Endpoints

- `GET /` - Message de bienvenue
- `GET /health` - Vérification de l'état de l'API
- `POST /items` - Créer un nouvel item

## Structure du projet

```
mon-api-fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── models.py
├── requirements.txt
├── render.yaml (optionnel)
└── README.md
```

## Déploiement

Le fichier `render.yaml` est configuré pour un déploiement sur Render.com.
