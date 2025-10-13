from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def get_intro():
    return {"message": "Hello Welcome to FastAPI"}
