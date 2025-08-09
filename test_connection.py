import asyncio
from app.data.database.supabase_client import supabase


async def test_supabase_connection():
    try:
        # Test simple : récupérer les tables
        response = supabase.table("gifts").select("*").execute()
        print("✅ Connexion Supabase réussie!")
        print(f"Nombre d'item: {response}")
    except Exception as e:
        print(f"❌ Erreur de connexion : {e}")


if __name__ == "__main__":
    asyncio.run(test_supabase_connection())
