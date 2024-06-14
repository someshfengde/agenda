from fastapi import APIRouter
from pydantic import BaseModel
from typing import List


router = APIRouter()

class CalendarEvent(BaseModel):
    title: str
    date: str
    time: str
    location: str
    description: str

@router.post("/post_events", response_model=CalendarEvent)
def create_event(event: CalendarEvent):
    return event

@router.get("/get_events", response_model=List[CalendarEvent])
def read_events():
    return []