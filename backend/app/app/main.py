import copy
from os import path
import random
import string
import time
import graypy
import logging
import json
from urllib.request import Request
from datetime import datetime

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings
from app.core.utils import read_bytes

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)

logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    #logger.info(f"rid={idem} start request path={request.url.path}")
    token = request.headers.get("authorization")
    #logger.info(f"rid={idem} application token: {token}")
    start_time = time.time()
    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)

    data = {
        "path": request.url.path,
        "speed": formatted_process_time,
        "token": token,
        "date": datetime.now(),

    }

    #content = await read_bytes(response.body_iterator)
    binary = b''
    copy_response = copy.deepcopy(response)
    async for data in copy_response.body_iterator:
        binary += data
    body = binary.decode()

    logger.info(body)

    # graylog = logging.getLogger("api_log")
    # graylog.setLevel(logging.INFO)
    # handler = graypy.GELFTCPHandler('10.0.0.105', 12201)
    # graylog.addHandler(handler)
    # graylog.info(json.dumps(str(request.headers.__dict__)))
    return response

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
