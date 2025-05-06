from fastapi import APIRouter
from app.services.birthday_service import get_employees_by_birthday

router = APIRouter()

@router.get("/birthday/{month}/{day}")
def birthday_employees(month: int, day: int, direction: str = "center", days: int = 14):
    return get_employees_by_birthday(month, day, direction, days)
