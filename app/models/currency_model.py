from pydantic import BaseModel, Field

class Currency(BaseModel):
    from_currency: str = Field(min_length=3, max_length=3, description="Origin currency")
    to_currency: str = Field(min_length=3, max_length=3,description="Destination currency" )
    amount_money: float = Field(gt=0, description="The amount should be greater than zero")

