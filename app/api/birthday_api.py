from fastapi import FastAPI, HTTPException
from services.birthday_service import get_employees_by_birthday
from datetime import datetime

app = FastAPI()

@app.get("/birthdays")
async def get_all_birthdays():
    try:
        employees = get_employees_by_birthday()
        return [{"name": emp["name"], "birthday": emp["birthday"]} for emp in employees]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/birthdays/{month}")
async def get_birthdays_by_month(month: int):
    try:
        employees = get_employees_by_birthday(month=month)
        return [{"name": emp["name"], "birthday": emp["birthday"]} for emp in employees]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/birthdays/{month}/{day}")
async def get_birthdays_by_month_day(month: int, day: int):
    try:
        employees = get_employees_by_birthday(month=month, day=day)
        return [{"name": emp["name"], "birthday": emp["birthday"]} for emp in employees]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
