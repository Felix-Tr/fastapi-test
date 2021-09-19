import math
import traceback
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from converter import int2str

class Convert(BaseModel):
    number: int


app = FastAPI()


@app.post("/convert/")
def converter(convert: Convert):
    """
    Handle integer to string request
    """

    if convert.number > 0:
        if math.log10(convert.number) >= 6:
            raise HTTPException(status_code=500, detail="Number is of order greater 6")

    # Get number string, if unexpected Error occures return as detail in Errormessage
    try:
        number_string = int2str(convert.number)
    except Exception:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {traceback.format_exc()}")

    response = {"number_string": number_string}

    return response
