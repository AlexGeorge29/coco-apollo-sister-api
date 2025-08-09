from fastapi import APIRouter, HTTPException
from app.data.database.supabase_client import supabase

router = APIRouter(prefix="/gifts", tags=["gifts"])


@router.get("/")
async def get_gifts():  # type: ignore
    try:
        response = supabase.table("gifts").select("*").execute()  # type: ignore
        return response.data
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Invalid gift data: {e}") from e
