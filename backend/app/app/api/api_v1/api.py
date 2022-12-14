from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils, keyword, domains, backlinks, url

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(keyword.router, prefix="/keywords", tags=["keywords"])
api_router.include_router(domains.router, prefix="/domains", tags=["Domains"])
api_router.include_router(backlinks.router, prefix="/backlinks", tags=["Baklinks Overview"])
api_router.include_router(url.router, prefix="/url", tags=["Urls"])

