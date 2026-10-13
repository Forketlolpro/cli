class AppError(Exception):
    pass


class ApiError(AppError):
    pass


VALID_CUR_LENGTH: int = 3


class ArgumentError(AppError):
    def __init__(self, invalid_currency: str) -> None:
        self.invalid_currency = invalid_currency

    def __str__(self) -> str:
        return f"не валидная валюта - {self.invalid_currency}"
