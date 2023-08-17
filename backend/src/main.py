import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def health_check():
    return {"Health check": "OK"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
