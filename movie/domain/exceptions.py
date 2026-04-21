from cinema.exceptions import DomainError


class MovieNotFoundError(DomainError):
    def __init__(self, movie_id: int):
        super().__init__(f"Фильм с id={movie_id} не найден")


class MovieSubscriptionMismatchError(DomainError):
    def __init__(self, move_id: int, subscription_id: int):
        super().__init__(f"Фильм с id={move_id} не соответствует подписке с id={subscription_id}")
