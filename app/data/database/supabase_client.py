from supabase import create_client, Client
from app.core.configs import configs

supabase: Client = create_client(configs.SUPABASE_URL, configs.SUPABASE_SERVICE_KEY)
supabase_admin: Client = create_client(
    configs.SUPABASE_URL, configs.SUPABASE_SERVICE_KEY
)
