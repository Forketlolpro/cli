import sys

from arguments import Arguments
from logging_config import setup_logging


def main(argv: list[str] | None = None) -> int:
    setup_logging()
    arguments = Arguments.get_arguments(argv)
    is_valid = arguments.validate()

    if not is_valid:
        sys.exit(1)

    return 0


if __name__ == "__main__":
    sys.exit(main())
