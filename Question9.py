"""
9-Global and Local variables: Run codes P1, P2, P3 and P4 and report outputs.
Explain reasons for their outputs in details.
"""
from fastapi import FastAPI

app = FastAPI()


def q9_p1():
    # P1
    def f():
        # local variable
        s1 = "I live in khorramabad"
        return s1

    # Main
    f()


def q9_p2():
    # P2
    try:
        def f():
            # local variable
            s2 = "I live in khorramabad"
            print("Inside Function:", s2)

        # Main
        f()
        return s2  # This will raise a NameError
    except NameError as e:
        # Catch the NameError and return it as a string
        return f"Error: {str(e)}"


def q9_p3():
    # P3
    def f():
        global s3
        s3 = 'I live in khorramabad.'
        print(s3)

    # Main: Global Scope
    s3 = 'I live in iran.'
    f()
    return s3


def q9_p4():
    # P4
    # This function uses global variable s
    def f():
        s4 = "I live in khorramabad."
        print(s4)

    # Main
    s4 = "I live in iran."
    f()
    return s4


@app.get("/q9/")
def question9_path_query():
    return {
        "Type result": "path parameter and query parameter",
        "result p1 is": q9_p1(),
        "result p2 is": q9_p2(),
        "result p3 is": q9_p3(),
        "result p4 is": q9_p4()
    }


@app.post("/q9/")
def question9_path_query():
    return {
        "Type result": "body",
        "result p1 is": q9_p1(),
        "result p2 is": q9_p2(),
        "result p3 is": q9_p3(),
        "result p4 is": q9_p4()
    }
