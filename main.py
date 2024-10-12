from fastapi import FastAPI
from app.routes import items, clock_in
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router)
app.include_router(clock_in.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI CRUD application!"}
