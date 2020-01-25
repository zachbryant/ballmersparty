from typing import List


class PROBLEM_TYPES:
    CODE = "code"
    MULTIPLE_CHOICE = "multiple-choice"


class ProblemSubmission:
    problem: "Problem"
    user: "User"
    game_session: "GameSession"

    def __init__(
        self,
        problem: "Problem",
        user: "User",
        game_session: "GameSession",
        submission_data,
    ):
        self.problem = problem
        self.user = user
        self.game_session = game_session
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

    @classmethod
    def load_problem_from_file(cls, filepath) -> "Problem":
        pass

    def construct_submission(
        self, user: "User", game_session: "GameSession", submission_data: object
    ):
        return PROBLEM_TYPE_TO_SUBMISSION_CLASS[self.type_](
            self, user, game_session, submission_data
        )


class ProblemManager:
    _problems: List[Problem]

    def __init__(self):
        pass  # load all problems here

    def _register_problem(self, problem: Problem):
        self._problems.append(problem)

    def pick_random_problem(self) -> Problem:
        pass
