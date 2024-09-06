from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logic.helpers as helpers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/random_year")
async def random_year():
    return {"year": helpers.randomYear()}

@app.get("/movie_from_year/{year}")
async def movie_from_year(year: int):
    return {"movie": helpers.movieFromYear(year)}

@app.get("/album_from_year/{year}")
async def album_from_year(year: int):
    albums = helpers.albumFromYear(year)
    return {"year": year, "albums": helpers.albumFromYear(year)}

@app.get("/invention_from_year/{year}")
async def invention_from_year(year: int):
    return {"invention": helpers.inventionFromYear(year)}

@app.get("/event_from_year/{year}")
async def event_from_year(year: int):
    return {"event": helpers.eventFromYear(year)}