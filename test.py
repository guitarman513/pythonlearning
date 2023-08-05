from typing import Generic, TypeVar, Optional

T = TypeVar('T', bool, int)  # T is either bool or int


class PopQuiz(Generic[T]):
    def __init__(self, value: T, subject: str, best_evaluation_score: int, is_pass_fail: bool) -> None:
        self.value: T = value
        self.subject: str = subject
        self.best_evaluation_score: int = best_evaluation_score
        self.is_pass_fail: bool = is_pass_fail


class ReportCard:
    def __init__(
            self, 
            gym: Optional[PopQuiz[bool]] = None, 
            art = None, 
            math = None, 
            science = None,
        ) -> None:
        self.gym: Optional[PopQuiz[bool]] = gym
        self.art: Optional[PopQuiz[bool]] = art
        self.math: Optional[PopQuiz[int]] = math
        self.science: Optional[PopQuiz[int]] = science


joe_grades = ReportCard()

joe_grades.math = PopQuiz(True, "Math", 60, False)

