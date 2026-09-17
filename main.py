from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strategy import generate_signal, simulate_price, portfolio, train_model

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Investing AI running"}

@app.get("/signal/{symbol}")
def signal(symbol: str):
    price = simulate_price(symbol)
    train_model()
    return generate_signal(symbol, price)

@app.get("/portfolio")
def get_portfolio():
    return portfolio
