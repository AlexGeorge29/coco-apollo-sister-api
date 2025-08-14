from typing import TypeVar, Generic, List, Dict, Any, Optional
from supabase import Client

T = TypeVar("T")


class SupabaseHelper(Generic[T]):
    def __init__(self, client: Optional[Client], table_name: str):
        if client is None:
            raise ValueError("Supabase client cannot be None")
        self.client = client
        self.table_name = table_name

    def get_all(self) -> List[Dict[str, Any]]:
        response = self.client.table(self.table_name).select("*").execute()
        return response.data
