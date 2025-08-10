from datetime import datetime, timezone


class TimestampMixin:
    created_at: str = datetime.now(timezone.utc).isoformat()
    updated_at: str = datetime.now(timezone.utc).isoformat()
