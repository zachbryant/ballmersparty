import os


SERVE_DIST = False

PROBLEMS_PATH = (
    os.environ["PROBLEMS_PATH"]
    if "PROBLEMS_PATH" in os.environ
    else os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "..", "..", "problem_tester", "problems"
    )
)

