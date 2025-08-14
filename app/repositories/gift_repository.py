from fastapi import HTTPException
from app.api.helpers.supabase_helpers import SupabaseHelper
from app.database import supabase_client


class GiftRepository:
    def __init__(self):
        self.client = supabase_client.supabase
        self.table = "gifts"

    def get_all(self) -> list[object]:
        """Retrieve all gifts from the database."""
        try:
            response = SupabaseHelper(self.client, self.table).get_all()
            # response = self.client.table("gifts").select("*").execute()  # type: ignore
            return response  # type: ignore
        except Exception as e:
            raise HTTPException(
                status_code=422, detail=f"Invalid gift data: {e}"
            ) from e
