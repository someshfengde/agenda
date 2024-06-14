from dotenv import load_dotenv

load_dotenv()
from fastapi import FastAPI
from agenda_backend.LLM_completion.groq_completions import get_groq_completions
from agenda_backend.calendar_events import router


app = FastAPI()

app.include_router(router, prefix="/api", tags=["events"])

@app.get("/llm_completion")
def read_llm_completion():
    return {"message": get_groq_completions()}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Magic by AgendaHero API"}