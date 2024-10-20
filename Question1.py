"""
1 - Write a program to get a number and print all its even digits separated by *.
Input: 822145635
Output: 6*4*2*2*8
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class NumberBody(BaseModel):
    number: int = 0


def q1(number: int):
    even_digits = [digit for digit in str(number) if int(digit) % 2 == 0]
    return '*'.join(even_digits)


@app.get("/q1/{number}")
def question1_path(number: int):
    result = q1(number)
    return {"result with (path parameter)": result}


@app.get("/q1/")
def question1_query(number: int):
    result = q1(number)
    return {"result with (query parameter)": result}


@app.post("/q1/")
def question1_body(number: NumberBody):
    result = q1(number.number)
    return {"result with (body)": result}

