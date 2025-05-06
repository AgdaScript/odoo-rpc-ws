from fastapi import FastAPI, HTTPException
from services.birthday_service import get_employees_by_birthday

app = FastAPI()

# Endpoint para pegar aniversariantes com base no filtro de mês e dia
@app.get("/birthdays")
async def get_birthday_employees(month: int, day: int):
    try:
        # Filtra os aniversariantes com base no mês e dia fornecido
        employees = get_employees_by_birthday(month, day)
        
        if not employees:
            raise HTTPException(status_code=404, detail="Nenhum aniversariante encontrado.")
        
        # Retorna os aniversariantes
        return [{"name": emp['name'], "birthday": emp['birthday']} for emp in employees]
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

