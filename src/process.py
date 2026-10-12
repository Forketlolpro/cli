import json
import logging

from arguments import Arguments
from exchange_rate_api import ExchangeResponse

logger = logging.getLogger(__name__)

def process_rates(exchange_rates: ExchangeResponse, arguments: Arguments) -> str:
    return json.dumps({
        "effective_date": exchange_rates["Date"],
        "requested_date": arguments.date or "null",
        "base_currency": "RUB",
        "rates": [
            {
                "currency": cur,
                "name": exchange_rates["Valute"][cur]["Name"],
                "rate": exchange_rates["Valute"][cur]["Value"],
            } for cur in arguments.currency if cur in exchange_rates["Valute"]
        ],
    }, ensure_ascii=False, indent=4)


