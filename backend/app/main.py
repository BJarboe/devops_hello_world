from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5000"],
    allow_methods=["GET","POST"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/hello")
async def hello():
    return {"message":"Hello from Python Backend!"}


def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)


if __name__ == '__main__':
    main()