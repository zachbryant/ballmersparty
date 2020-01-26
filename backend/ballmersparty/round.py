from .problem import Problem, ProblemSubmissionCode
from .user import User

from typing import Dict

DEFAULT_ROUND_TIME = 900  # default of 15 minutes a.k.a. 900 seconds
DEFAULT_CRUNCH_TIME = 180  # default of 3 minutes a.k.a. 180 seconds


class Round:

    user_stats: Dict[User, "UserRoundStats"]  # Active games
    user_ready: Dict[User, bool]

    def __init__(self, users, problem, game_session):
        self.problem = problem
        self.game_session = game_session
        self.total_time = DEFAULT_ROUND_TIME
        self.crunch_time = DEFAULT_CRUNCH_TIME
        self.first_passed_user = None  # User that passes the first test case
        self.user_stats = {}
        self.user_ready = {}

        for user in users:
            self.user_stats[user] = UserRoundStats(user)
            self.user_ready[user] = False

    def set_user_ready(self, user):
        self.user_ready[user] = True

    def is_everyone_ready(self):
        return all(map(lambda key: self.user_ready[key], self.user_ready))

    def get_problem_description(self):
        return {"name": self.problem.name, "description": self.problem.description}

    async def submission(self, user: User, submission_data):

        # TODO: Need to make the submission have filed lines and test_cases_passed

        submission = ProblemSubmissionCode(self.problem, user, submission_data)
        await submission.process()
        self.user_stats[user].update_stats(submission)

        # Logic for first user passed a test case
        if self.first_passed_user == None and submission.test_cases_passed > 0:
            self.first_passed_user = user
            self.user_stats[user].first_to_pass()
            # TODO: Start crunch time timer and notify users

        if submission.test_cases_passed == self.problem.total_cases:
            self.user_stats[user].passed_all_cases(self.total_time, self.crunch_time)


class UserRoundStats:

    CASE_POINT_WORTH = 10  # Amount of points passing a test case is worth

    def __init__(self, user: User):
        self.user = user
        self.compiles = 0
        self.submission_lines = 0
        self.test_cases_passed = 0
        self.first_to_pass_flag = False
        self.passed_all_cases_flag = False

    def update_stats(self, submission):
        self.compiles += 1
        self.submission_lines = submission.lines
        self.test_cases_passed = submission.test_cases_passed

    def first_to_pass(self):
        first_to_pass_flag = True

    def passed_all_cases(self, total_time, crunch_time):
        passed_all_cases_flag = True
        self.time_taken = (DEFAULT_ROUND_TIME - total_time) + (
            DEFAULT_CRUNCH_TIME - crunch_time
        )

    def get_total_points(self):
        total_points = test_cases_passed * CASE_POINT_WORTH
        if first_to_pass_flag:
            total_points += 10
        if passed_all_cases_flag:
            total_points += 10

        return total_points

