"""
10-Study about Recursive Functions in python.
Explain in details that how does the following recursive function work?
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


def factorial(x: int):
    if x == 1:  # This is the base case
        return 1
    else:  # This is the recursive case
        return x * factorial(x - 1)


class FactorialBody(BaseModel):
    number: int


@app.get("/q10/{number}")
async def question10_path(number: int):
    if number < 1:
        return {"error": "The number should be greater than 0"}
    else:
        result = factorial(number)
        return {
            "Type result": "path parameter",
            "Factorial": result
        }


@app.get("/q10/")
async def question10_query(number: int):
    if number < 1:
        return {"error": "The number should be greater than 0"}
    else:
        result = factorial(number)
        return {
            "Type result": "query parameter",
            "Factorial": result
        }


@app.post("/q10/")
async def question10_body(data: FactorialBody):
    number = data.number
    if number < 1:
        return {"error": "The number should be greater than 0"}
    else:
        result = factorial(number)
        return {
            "Type result": "body",
            "Factorial": result
        }