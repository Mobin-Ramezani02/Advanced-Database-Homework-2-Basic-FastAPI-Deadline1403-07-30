"""
2 - Write a program to compute the following expression for 500 sentences:
(3! / 2+9) − (5! / 3+7) + (7! / 4+5) − (9! / 5+3) + (11! / 6+1) − (13! 7−1) …
"""

from fastapi import FastAPI
from pydantic import BaseModel
import math
from decimal import Decimal

app = FastAPI()


class NumberBody(BaseModel):
    n: int = 0


def q2(number: int):
    result = Decimal(0)
    sign = -1
    for i in range(number):
        sign *= -1
        numerator = (2 * i) + 3
        denominator = Decimal(i + 2) + Decimal(9 - (2 * i))

        if denominator == 0:
            continue

        term_value = Decimal(math.factorial(numerator) / denominator)
        result += Decimal(sign) * term_value

    return result


@app.get("/q2/{n}")
async def question2_path(n: int):
    result = q2(n)
    return {"result with (path parameter)": result}


@app.get("/q2/")
async def question2_query(n: int):
    result = q2(n)
    return {"result with (query parameter)": result}


@app.post("/q2/")
async def question2_body(n: NumberBody):
    result = q2(n.n)
    return {"result with (body)": result}
