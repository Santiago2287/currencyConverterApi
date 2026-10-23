import httpx
from app.services.exceptions import CurrencyNetworkError, CurrencyDataError

async def get_converted_amount(from_currency: str, to_currency: str, amount: float) -> dict:
    #formamos la cadena del cosulta

    #cadena mal complicada para mantener
    #url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    
    #base url
    url = "https://api.frankfurter.app/latest"
    #define of paramethods for using
    paramethods = {
        "amount":amount,
        "from":from_currency.upper(),
        "to":to_currency.upper()
    }

    async with httpx.AsyncClient(timeout=10.0, follow_redirects=True) as client:
        try:
            response = await client.get(url, params=paramethods)
            response.raise_for_status()

            datos = response.json()

            # INSPECCIÓN DE INGENIERÍA: Imprimimos la respuesta real en la consola de uvicorn
            print("\n=== DEBUG BANCO ===")
            print("Datos recibidos:", datos)
            print("Buscando moneda:", to_currency.upper())
            print("===================\n")

            if "rates" not in datos or paramethods["to"] not in datos["rates"]:
                raise CurrencyDataError("The bank sent we, but the currency formant is unacceptable")
            return datos["rates"][to_currency.upper()]
        
        except httpx.HTTPStatusError as e:
                if e.response.status_code == 404:
                    raise ValueError("One currency input no is can't stand procesing")
                raise CurrencyNetworkError(f"El servidor del banco rebotó la conexión con error: {e.response.status_code}")
            
        except httpx.RequestError as e:
            raise CurrencyNetworkError(f"Falla de red (¿Sin WiFi o API caída?): {e}")
        
        except ValueError as e:
            raise e