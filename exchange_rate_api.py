import logging
from dataclasses import dataclass
from typing import TypedDict

import requests

from arguments import Arguments

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
        return url.format(year, month, day)


class Valute(TypedDict):
    CharCode: str
    ID: str
    Name: str
    Nominal: str
    NumCode: str
    Previous: str
    value: str
    Value: str

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
    ### Вот тут правильно ли я обрабатываю ошибки?
    except requests.exceptions.RequestException as err:
        logger.info("RequestException: %s", err)
        raise

    data: ExchangeResponse = response.json()
    return data


def get_exchange_params_from_arguments(arguments: Arguments) -> ExchangeRateParams:
    return ExchangeRateParams(arguments.date)


def fetch_exchange_rates(arguments: Arguments) -> ExchangeResponse:
    params = get_exchange_params_from_arguments(arguments)
    return exchange_rate_api(params)
