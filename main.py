import logging
import sys

from arguments import Arguments
from exchange_rate_api import fetch_exchange_rates
from logging_config import setup_logging

logger = logging.getLogger(__name__)


def main(argv: list[str] | None = None) -> int:
    try:
        setup_logging()
        arguments = Arguments.get_arguments(argv)
        is_valid = arguments.validate()

        if not is_valid:
            sys.exit(1)

        exchange_rates = fetch_exchange_rates(arguments)
        print(exchange_rates)
    ## Один централизованный обработчик ошибок. Правильно ли это?
    except Exception as e:
        logger.info("Handle error in main: %s", e)
        sys.exit(1)

    return 0


if __name__ == "__main__":
    sys.exit(main())
