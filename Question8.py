"""
8 - Give a number with 5 digits in main. If the number is not a 5 digits number, ask repeatedly from user
to enter a valid number. Send the number for F1 function to find and return the maximum digit of the number.
In the next step, send the maximum digit and the input number for F2 function to delete the maximum digit from
number and return it. Finally, print the final output in main as shown in figure below.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class NumberBody(BaseModel):
    number: int


def F1(number: int):
    digits = []
    while number > 0:
        digit = number % 10
        digits.append(digit)
        number //= 10
    max_digit = max(digits)
    return max_digit


def F2(number: int, digit: int):
    number = str(number).replace(f"{digit}", "").strip()
    return number


@app.get("/q8/{number}")
def question8_path(number: int):
    if len(str(number)) == 5:
        max_digit = F1(number)
        final_number = F2(number, max_digit)
        return {
            "Type result": "path parameter",
            "Maximum digit": max_digit,
            f"Final number without {max_digit}": final_number
        }
    else:
        return {"error": "The number is not 5 digits"}


@app.get("/q8/")
def question8_query(number: int):
    if len(str(number)) == 5:
        max_digit = F1(number)
        final_number = F2(number, max_digit)
        return {
            "Type result": "query parameter",
            "Maximum digit": max_digit,
            f"Final number without {max_digit}": final_number
        }
    else:
        return {"error": "The number is not 5 digits"}


@app.post("/q8/")
def question8_body(data: NumberBody):
    number = data.number
    if len(str(number)) == 5:
        max_digit = F1(number)
        final_number = F2(number, max_digit)
        return {
            "Type result": "body",
            "Maximum digit": max_digit,
            f"Final number without {max_digit}": final_number
        }
    else:
        return {"error": "The number is not 5 digits"}
