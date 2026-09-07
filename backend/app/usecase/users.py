from typing import Annotated

from fastapi import APIRouter, Depends

from app.domains.users.userservice import UserService, get_user_service

user_router = APIRouter()


@user_router.get("/")
async def get_users(
    service: Annotated[UserService, Depends(get_user_service)],
) -> list[str]:
    return service.get_users()
