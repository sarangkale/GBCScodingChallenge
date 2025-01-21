from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for the request body
class InternDetails(BaseModel):
    name: str
    studying: str
    age: int
    hobbies: List[str]

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Define a POST endpoint to receive intern details
@app.post("/interns/")
def create_intern(intern: InternDetails):
    return {"message": "Intern details received", "intern": intern}
