from os import path
import uvicorn
import time
import graypy
import logging
import traceback
from urllib.request import Request

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response

from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)

logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    token = request.headers.get("authorization")
    start_time = time.time()
    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)

    data = {
        "path": request.url.path,
        "speed": formatted_process_time,
        "token": token
    }

    graylog = logging.getLogger("api_log")
    graylog.setLevel(logging.INFO)
    handler = graypy.GELFTCPHandler(settings.GRAYLOG_SERVER, settings.GRAYLOG_PORT)
    graylog.addHandler(handler)
    adapter = logging.LoggerAdapter(logging.getLogger("api_log"), {"request": request.__dict__})
    adapter.info(data)
    return response


@app.middleware("http")
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        # you probably want some kind of logging here
        graylog = logging.getLogger("api_exception")
        graylog.setLevel(logging.ERROR)
        handler = graypy.GELFTCPHandler(settings.GRAYLOG_SERVER, settings.GRAYLOG_PORT)
        graylog.addHandler(handler)
        adapter = logging.LoggerAdapter(logging.getLogger("api_exception"), {"request": request.__dict__})
        adapter.error(traceback.format_exc())
        return Response("Internal server error", status_code=500)


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
