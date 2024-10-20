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
    change_sign = True
    sign = Decimal(1)
    fact_start = 3
    first_num = 2
    second_num = 9
    result = Decimal(0)

    for _ in range(number):
        fact = Decimal(math.factorial(fact_start))
        denominator = Decimal(first_num + second_num)

        if denominator == 0:
            continue
        else:
            result += sign * (fact / denominator)

        fact_start += 2
        first_num += 1
        second_num -= 2

        if change_sign:
            sign = Decimal(-1)
            change_sign = False
        else:
            sign = Decimal(1)
            change_sign = True

    return result


@app.get("/q2/{n}")
def question2_path(n: int):
    result = q2(n)
    return {"result with (path parameter)": result}


@app.get("/q2/")
def question2_query(n: int):
    result = q2(n)
    return {"result with (query parameter)": result}


@app.post("/q2/")
def question2_body(n: NumberBody):
    result = q2(n.n)
    return {"result with (body)": result}
