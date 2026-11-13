from fastapi import APIRouter

router_get_users = APIRouter()

@router_get_users.get("/users")
async def get_users():
    return [
        {'id': 1, 'name': 'Bartosz K'},
        {'id': 2, 'name': 'Bartosz W'},
        {'id': 3, 'name': 'Emil'},
        {'id': 4, 'name': 'Mikołaj'},
        {'id': 5, 'name': 'Natalia'}
    ]