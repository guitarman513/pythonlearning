from typing import Optional


class PopQuiz:
    def __init__(self, subject: str, best_evaluation_score: int, test_day: str) -> None:
        self.subject: str = subject
        self.best_evaluation_score: int = best_evaluation_score
        self.test_day: str = test_day
    def __repr__(self):
        return f'{self.subject} score: {self.best_evaluation_score}'


class ReportCard:
    def __init__(
            self, 
            gym: Optional[PopQuiz] = None, 
            art: Optional[PopQuiz] = None, 
            math: Optional[PopQuiz] = None, 
            science: Optional[PopQuiz] = None, 
        ) -> None:
        self.gym: Optional[PopQuiz] = gym
        self.art: Optional[PopQuiz] = art
        self.math: Optional[PopQuiz] = math
        self.science: Optional[PopQuiz] = science


joe_grades = ReportCard()

joe_grades.math = PopQuiz("Math", 60, "Monday")
joe_grades.math = PopQuiz("Math", 50, "Monday")

joe_grades.math
