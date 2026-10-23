from fastapi import APIRouter, HTTPException
from app.models.currency_model import Currency
from app.services.currency_engine import get_converted_amount, CurrencyNetworkError, CurrencyDataError

router = APIRouter(prefix="/api/v1/currency", tags=["Currency of converte"])

@router.post("/convert")
async def convert_currency(request: Currency):
    try:
        result = await get_converted_amount(from_currency=request.from_currency, to_currency=request.to_currency, amount=request.amount_money)

        return {
            "success":True,
            "original":f"{request.amount_money} {request.from_currency.upper()}",
            "convert":f"{result} {request.to_currency.upper()}"
        }
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        
    except CurrencyDataError as e:
        raise HTTPException(status_code=422, detail=str(e))
        
    except CurrencyNetworkError as e:
        raise HTTPException(status_code=503, detail=str(e)) 
