from typing import List
from .config import PROBLEMS_PATH
import os
import random
import json


def load_problem_paths():
    return list(
        map(lambda x: os.path.join(PROBLEMS_PATH, x), os.listdir(PROBLEMS_PATH))
    )


PROBLEMS_LIST = load_problem_paths()

def validate_problem_structure():
    for path in PROBLEMS_LIST:
        Problem.load_problem_from_file(path)


class PROBLEM_TYPES:
    CODE = "code"
    MULTIPLE_CHOICE = "multiple-choice"


class ProblemSubmission:
    problem: "Problem"
    user: "User"
    game_session: "GameSession"

    def __init__(self, problem: "Problem", user: "User", submission_data):
        self.problem = problem
        self.user = user
        self.submission_data = submission_data

    def validate(self):
        raise NotImplementedError


class ProblemSubmissionCode(ProblemSubmission):
    pass


class ProblemSubmissionMultipleChoice(ProblemSubmission):
    pass


PROBLEM_TYPE_TO_SUBMISSION_CLASS = {
    PROBLEM_TYPES.CODE: ProblemSubmissionCode,
    PROBLEM_TYPES.MULTIPLE_CHOICE: ProblemSubmissionMultipleChoice,
}


class Problem:
    type_: str
    spec: object


    def __init__(self, spec, description, path):
        self.spec = spec
        self.description = description
        self.path = path

    @classmethod
    def load_problem_from_file(cls, filepath) -> "Problem":
        with open(os.path.join(filepath, 'spec.json'), 'r') as f:
            spec = json.load(f)

        with open(os.path.join(filepath, 'description.md'), 'r') as f:
            description = f.read()

        return cls(spec, description, filepath)

    def construct_submission(
        self, user: "User", game_session: "GameSession", submission_data: object
    ):
        return PROBLEM_TYPE_TO_SUBMISSION_CLASS[self.type_](
            self, user, game_session, submission_data
        )


class ProblemManager:
    _picked_problem_paths: List[str] = []

    def pick_random_problem(self) -> Problem:
        problem_path = random.choice(PROBLEMS_LIST)
        while problem_path in self._picked_problem_paths:
            problem_path = random.choice(PROBLEMS_LIST)

        self._picked_problem_paths.append(problem_path)

        return Problem.load_problem_from_file(problem_path)

