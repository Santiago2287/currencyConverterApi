from fastapi import FastAPI
from app.routers import currency_route

app = FastAPI(
    title="Currency Converter API",
    description="Assync API for quering Currency converter in real time",
    version="1.0.0")

app.include_router(currency_route.router)

@app.get("/")
async def root():
    return {"message":"You are consumming the CurrencyConverterApi, You can go to documentation for interacting"}