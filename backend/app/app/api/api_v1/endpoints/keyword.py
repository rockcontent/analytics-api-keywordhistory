from typing import Any, List
from python_semrush.semrush import SemrushClient

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()



#client = SemrushClient(key='your_semrush_api_key')
#result = client.domain_ranks(domain='example.com')