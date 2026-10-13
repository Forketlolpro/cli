import json
import logging
from decimal import ROUND_HALF_UP, Decimal

from currency_rates.exchange_rate_api import ExchangeResponse

logger = logging.getLogger(__name__)


def process_rates(exchange_rates: ExchangeResponse, *, date: str | None, currency: list[str]) -> str:
    rates = []
    for cur in currency:
        if cur not in exchange_rates["Valute"]:
            continue
        raw_cur = exchange_rates["Valute"][cur]
        rate = Decimal(raw_cur["Value"]) / Decimal(raw_cur["Nominal"])
        rates.append(
            {
                "currency": cur,
                "name": raw_cur["Name"],
                "rate": rate.quantize(Decimal("1.000000"), ROUND_HALF_UP),
            },
        )

    return json.dumps(
        {
            "effective_date": exchange_rates["Date"],
            "requested_date": date or "null",
            "base_currency": "RUB",
            "rates": rates,
        },
        ensure_ascii=False,
        indent=4,
        default=str,
    )
