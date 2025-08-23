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

    def get_by_id(self, id_to_get: int) -> Optional[Dict[str, Any]]:
        response = (
            self.client.table(self.table_name).select("*").eq("id", id_to_get).execute()
        )
        return response.data[0] if response.data else None

    def get_by_field(
        self, field_name: str, field_value: Any
    ) -> Optional[List[Dict[str, Any]]]:
        response = (
            self.client.table(self.table_name)
            .select("*")
            .eq(field_name, field_value)
            .execute()
        )
        return response.data if response.data else []

    def create(self, item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        response = self.client.table(self.table_name).insert(item).execute()  # type: ignore
        return response.data[0] if response.data else None

    def delete(self, id_to_delete: int) -> None:
        self.client.table(self.table_name).delete().eq("id", id_to_delete).execute()

    def update(
        self, id_to_update: int, item: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        response = (
            self.client.table(self.table_name)
            .update(item)  # type: ignore
            .eq("id", id_to_update)
            .execute()
        )
        return response.data[0] if response.data else None
