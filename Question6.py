"""
6 - Write a program to get n and then n numbers from user and compute maximum, minimum, average and
standard deviation. Test your program for 5 different inputs.
input:                          output:
Enter the n:5                   Maximum is: 84
Enter number 1:12               Minimum is: 9
Enter number 2:15               Average is: 26.2
Enter number 3:9                Standard Deviation is: 28.96
Enter number 4:11
Enter number 5:84
"""
from fastapi import FastAPI
from pydantic import BaseModel
import math

app = FastAPI()


class NumbersBody(BaseModel):
    numbers: list[float]


def q6(numbers: list[float]):
    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)
    variance = sum((x - average) ** 2 for x in numbers) / len(numbers)
    std = math.sqrt(variance)
    return maximum, minimum, average, std


@app.get("/q6/{numbers}")
def question6_path(numbers: str):
    number_list = list(map(float, numbers.split(',')))
    maximum, minimum, average, std = q6(number_list)
    return {
        "Type result": "path parameter",
        "Maximum": maximum,
        "Minimum": minimum,
        "Average": float(f"{average:.4f}"),
        "Standard Deviation": float(f"{std:.4f}")
    }


@app.get("/q6/")
def question6_query(numbers: str):
    number_list = list(map(float, numbers.split(',')))
    maximum, minimum, average, std = q6(number_list)
    return {
        "Type result": "query parameter",
        "Maximum": maximum,
        "Minimum": minimum,
        "Average": float(f"{average:.4f}"),
        "Standard Deviation": float(f"{std:.4f}")
    }


@app.post("/q6/")
def question6_body(numbers_body: NumbersBody):
    numbers = numbers_body.numbers
    maximum, minimum, average, std = q6(numbers)
    return {
        "Type result": "body",
        "Maximum": maximum,
        "Minimum": minimum,
        "Average": float(f"{average:.4f}"),
        "Standard Deviation": float(f"{std:.4f}")
    }
