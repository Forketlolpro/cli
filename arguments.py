from __future__ import annotations

import argparse

import time_utils


class Arguments(argparse.Namespace):
    currency: list[str]
    date: str | None

    def validate(self) -> bool:
        return True

    def __str__(self) -> str:
        return f"[Arguments]: \n currency: {self.currency} \n date: {self.date}"

    @staticmethod
    def get_arguments(argv: list[str] | None = None) -> Arguments:
        parser = argparse.ArgumentParser(
            description="My cli app arguments parser",
        )

        parser.add_argument(
            "-currency",
            nargs="+",
            choices=["USD", "RUB", "EUR", "CNY"],
            required=True,
            help="Укажите одну или несколько валют через пробел (например: USD RUB)",
        )

        parser.add_argument(
            "-d",
            "--date",
            type=str,
            help="за определенную дату",
            default=time_utils.get_local_day(),
        )

        return parser.parse_args(argv, namespace=Arguments())
