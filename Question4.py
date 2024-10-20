"""
4 - Write a program to print all 3 digits numbers (between a 100 and 999) that does not have odd digits.
Consider 0 as even digit.
Output: 200, 202,204, 206,208,220,222,…
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class RangeBody(BaseModel):
    start: int = 100
    end: int = 999


def q4(start: int, end: int):
    results = []
    for num in range(start, end):
        number = str(num)
        digit1 = int(number[0])
        digit2 = int(number[1])
        digit3 = int(number[2])
        if digit1 % 2 == 0 and digit2 % 2 == 0 and digit3 % 2 == 0:
            results.append(num)
    return results


@app.get("/q4/{start}-{end}")
def question4_path(start: int, end: int):
    results = q4(start, end)
    return {"result with (path parameter)": results}


@app.get("/q4/")
def question4_query(start: int, end: int):
    results = q4(start, end)
    return {"result with (query parameter)": results}


@app.post("/q4/")
def question4_body(range_body: RangeBody):
    results = q4(range_body.start, range_body.end)
    return {"result with (body)": results}
