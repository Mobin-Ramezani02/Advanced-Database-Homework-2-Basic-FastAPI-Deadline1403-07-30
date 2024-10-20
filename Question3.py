"""
3 - Write a program to print all 4 digits numbers (between 1000 and 9999) that the sum of the first
and second digits is equal with the product of the third and forth digits.
3466: 6 + 6 = 3 × 4
Output: 1110, 1101, ..., 2999 , ... , 3466 , ...
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class RangeBody(BaseModel):
    start: int = 1000
    end: int = 10000


def q3(start: int, end: int):
    results = []
    for num in range(start, end):
        number = str(num)
        digit1 = int(number[0])
        digit2 = int(number[1])
        digit3 = int(number[2])
        digit4 = int(number[3])
        if digit1 + digit2 == digit3 * digit4:
            results.append(num)
    return results


@app.get("/q3/{start}-{end}")
def question3_path(start: int, end: int):
    results = q3(start, end)
    return {"result with (path parameter)": results}


@app.get("/q3/")
def question3_query(start: int, end: int):
    results = q3(start, end)
    return {"result with (query parameter)": results}


@app.post("/q3/")
def question3_body(range_body: RangeBody):
    results = q3(range_body.start, range_body.end)
    return {"result with (body)": results}

