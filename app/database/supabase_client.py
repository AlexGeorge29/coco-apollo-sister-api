from supabase import create_client, Client
from app.core.config.configs import configs


class SupabaseClient:
    _instance = None
    _client = None
    _admin_client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._client is None:
            if (
                hasattr(configs, "SUPABASE_SERVICE_KEY")
                and configs.SUPABASE_SERVICE_KEY
            ):
                if configs.SUPABASE_URL:
                    self._client = create_client(
                        configs.SUPABASE_URL, configs.SUPABASE_SERVICE_KEY
                    )
            if configs.SUPABASE_URL and configs.SUPABASE_SERVICE_KEY:
                self._admin_client = create_client(
                    configs.SUPABASE_URL, configs.SUPABASE_SERVICE_KEY
                )

    @property
    def client(self) -> Client | None:
        if self._client is not None:
            return self._client or self._admin_client


_supabase_client = SupabaseClient()
supabase: Client | None = _supabase_client.client
