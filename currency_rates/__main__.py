import logging
import sys

from currency_rates.arguments import Arguments
from currency_rates.errors import AppError
from currency_rates.exchange_rate_api import fetch_exchange_rates
from currency_rates.logging_config import setup_logging
from currency_rates.process import process_rates
from currency_rates.writer import writer_into_file

logger = logging.getLogger(__name__)


def main(argv: list[str] | None = None) -> int:
    try:
        setup_logging()
        arguments = Arguments.get_arguments(argv)
        arguments.validate()

        exchange_rates = fetch_exchange_rates(arguments)
        writer_into_file(
            process_rates(exchange_rates, date=arguments.date, currency=arguments.currencies),
            arguments.output,
        )
    ## Один централизованный обработчик ошибок. Правильно ли это?
    except AppError:
        logger.exception("App error")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
