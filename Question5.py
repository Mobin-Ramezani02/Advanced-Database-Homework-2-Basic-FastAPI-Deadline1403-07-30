"""
5 - Write a program to get n from user and print the following pattern:
Input: n=8
Output:
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
6 12 18 24 30 36
7 14 21 28 35 42 49
8 16 24 32 40 48 56 64
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PatternBody(BaseModel):
    n: int = 8


def q5(n: int):
    result = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            row.append(i * j)
        result.append(row)
    return result


@app.get("/q5/{n}")
def question5_path(n: int):
    result = q5(n)
    return {"result with (path parameter)": result}


@app.get("/q5/")
def question5_query(n: int):
    result = q5(n)
    return {"result with (query parameter)": result}


@app.post("/q5/")
def question5_body(pattern_body: PatternBody):
    result = q5(pattern_body.n)
    return {"result with (body)": result}
