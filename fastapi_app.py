from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time, jwt  # pip install PyJWT
# from jose import jwt

# --- demo creds (replace with DB later)
# DEMO_USERNAME = "admin"
# DEMO_PASSWORD = "1234"
# SECRET = "use-a-long-random-secret"
# ALGO = "HS256"

USERS = {"admin": "1234"}

app = FastAPI()

# Allow your React dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginIn(BaseModel):
    username: str
    password: str

class LoginOut(BaseModel):
    ok: bool
    user: str | None = None
    message: str

@app.post("/login", response_model=LoginOut)
# def login(payload: LoginIn):
#     if payload.username == USERS and payload.password == USERS:
#         # optional: return JWT
#         token = jwt.encode({"sub": payload.username, "exp": int(time.time()) + 3600}, SECRET, algorithm=ALGO)
#         return {"ok": True, "access_token": token, "token_type": "bearer"}
#     raise HTTPException(status_code=401, detail="Invalid credentials")

def login(payload: LoginIn):
    if USERS.get(payload.username) == payload.password:
        return LoginOut(ok=True, user=payload.username, message="Login successful")
    raise HTTPException(status_code=401, detail="Invalid username or password")