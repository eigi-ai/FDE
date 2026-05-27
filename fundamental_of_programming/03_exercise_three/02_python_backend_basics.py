"""Runnable examples for Part 2: imports and exception handling.

Read `02_python_backend_basics.md` first for the full theory.
This Python file is only for code examples and printed output.
"""


def import_examples():
    # Demonstrate two common import styles used in Python.
    import math

    print("--- Import Examples ---")
    print(f"Square root of 25: {math.sqrt(25)}")

    from json import dumps

    sample = {"topic": "imports", "status": "easy"}
    print(f"JSON string: {dumps(sample)}")
    print()


def exception_examples():
    # Show basic success and failure handling with try/except/else/finally.
    print("--- Exception Handling Examples ---")

    try:
        number = int("10")
        print(f"Converted value: {number}")
    except ValueError:
        print("The value could not be converted to an integer.")
    else:
        print("Conversion worked without errors.")
    finally:
        print("This block always runs.")

    print()

    try:
        result = 10 / 0
        print(result)
    except ZeroDivisionError:
        print("You cannot divide a number by zero.")

    print()


def explain_try_except_in_detail():
    # Show how different exception branches can handle different failure types.
    print("--- Try/Except In Detail ---")
    print("In Python, the correct term is try/except, not try/catch.")
    print("try: write code that may fail.")
    print("except: handle the error safely.")
    print("else: run success-only code when no error occurs.")
    print("finally: run cleanup code no matter what happens.")
    print()

    print("Example of multiple except blocks:")

    try:
        data = {"name": "Aarav"}
        age = data["age"]
        print(age)
    except KeyError:
        print("The expected key is missing from the dictionary.")
    except TypeError:
        print("The data type is not what we expected.")
    finally:
        print("Finished checking dictionary data.")

    print()


def api_exception_note():
    # Summarize why backend code needs robust exception handling.
    print("--- Why Try/Except Matters In Backend Work ---")
    print("When a backend calls another API, many failures are possible:")
    print("- network failure")
    print("- timeout")
    print("- invalid JSON")
    print("- missing fields in response")
    print("- authentication failure")
    print("That is why backend engineers must understand try/except clearly.")
    print()


def backend_file_structure_note():
    # Explain why imports matter once backend code is split into modules.
    print("--- Backend File Structure Note ---")
    print(
        "In real backend projects, imports connect route files, service files, config files, and utility files."
    )
    print("That is why import is a core topic before FastAPI.")
    print()


if __name__ == "__main__":
    import_examples()
    exception_examples()
    explain_try_except_in_detail()
    api_exception_note()
    backend_file_structure_note()
