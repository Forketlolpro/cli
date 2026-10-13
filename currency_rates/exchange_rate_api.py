import logging
from dataclasses import dataclass
from typing import TypedDict

import requests

from currency_rates.arguments import Arguments
from currency_rates.errors import ApiError

logger = logging.getLogger(__name__)

url = "https://www.cbr-xml-daily.ru/daily_json.js"
daly_url = "https://www.cbr-xml-daily.ru/archive/{0}/{1}/{2}/daily_json.js"


@dataclass
class ExchangeRateParams:
    date: str | None

    def get_url(self) -> str:
        if self.date is None:
            return url
        year, month, day = self.date.split("-")
        return daly_url.format(year, month, day)


class Valute(TypedDict):
    CharCode: str
    ID: str
    Name: str
    Nominal: int
    NumCode: str
    Previous: float
    Value: float


class ExchangeResponse(TypedDict):
    Date: str
    PreviousDate: str
    PreviousURL: str
    Timestamp: str
    Valute: dict[str, Valute]


def exchange_rate_api(param: ExchangeRateParams) -> ExchangeResponse:
    try:
        response = requests.get(param.get_url(), timeout=10)
        response.raise_for_status()
        data: ExchangeResponse = response.json()
        logger.info(data)
    except requests.exceptions.RequestException as err:
        raise ApiError(err) from err

    return data


def get_exchange_params_from_arguments(arguments: Arguments) -> ExchangeRateParams:
    return ExchangeRateParams(arguments.date)


def fetch_exchange_rates(arguments: Arguments) -> ExchangeResponse:
    params = get_exchange_params_from_arguments(arguments)
    return exchange_rate_api(params)
