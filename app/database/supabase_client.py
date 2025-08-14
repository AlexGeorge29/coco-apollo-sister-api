from supabase import create_client, Client
from app.core.config.configs import configs


class SupabaseClient:
    """Client Supabase simple avec singleton pattern"""

    _instance = None
    _client = None
    _admin_client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._client is None:
            # Client normal (anon key)
            if (
                hasattr(configs, "SUPABASE_SERVICE_KEY")
                and configs.SUPABASE_SERVICE_KEY
            ):
                self._client = create_client(
                    configs.SUPABASE_URL, configs.SUPABASE_SERVICE_KEY
                )

            # Client admin (service key)
            self._admin_client = create_client(
                configs.SUPABASE_URL, configs.SUPABASE_SERVICE_KEY
            )

    @property
    def client(self) -> Client | None:
        """Client normal ou fallback admin"""
        if self._client is not None:
            return self._client or self._admin_client


_supabase_client = SupabaseClient()

supabase: Client | None = _supabase_client.client
