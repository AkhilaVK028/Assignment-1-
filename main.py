import uvicorn
from fastapi import FastAPI
from Scripts.core.services.service import app as crud


app = FastAPI()
app.include_router(crud)


if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=int(8034))
