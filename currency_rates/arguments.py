from __future__ import annotations

import argparse

from currency_rates.errors import VALID_CUR_LENGTH, ArgumentError
from currency_rates.time_utils import get_local_day


class Arguments(argparse.Namespace):
    currencies: list[str]
    date: str | None
    output: str

    def validate(self) -> None:
        invalid_currency = next((curr for curr in self.currencies if len(curr) != VALID_CUR_LENGTH), None)
        if invalid_currency:
            raise ArgumentError(invalid_currency)

    def __str__(self) -> str:
        return f"[Arguments]: \n currency: {self.currency} \n date: {self.date}"

    @staticmethod
    def get_arguments(argv: list[str] | None = None) -> Arguments:
        parser = argparse.ArgumentParser(
            description="My cli app arguments parser",
        )

        parser.add_argument(
            "--currencies",
            nargs="+",
            type=str,
            required=True,
            help="Укажите одну или несколько валют через пробел (например: USD RUB)",
        )

        parser.add_argument(
            "-d",
            "--date",
            type=str,
            help="за определенную дату",
            default=get_local_day(),
        )

        parser.add_argument(
            "-o",
            "--output",
            type=str,
            help="Имя файла",
            default="rates.json",
        )

        return parser.parse_args(argv, namespace=Arguments())
