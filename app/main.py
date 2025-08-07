from fastapi import FastAPI
from .models import Item, ItemResponse

app = FastAPI(
    title="Mon API FastAPI",
    description="Une API simple créée avec FastAPI",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {"message": "Bienvenue dans mon API FastAPI!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.post("/items", response_model=ItemResponse)
async def create_item(item: Item):
    return ItemResponse(
        id=1,
        name=item.name,
        description=item.description,
        price=item.price,
        message="Item créé avec succès",
    )
