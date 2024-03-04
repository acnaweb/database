import logging
import argparse

LOG_FORMAT = "%(asctime)s %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

action_choices = ["action1", "action2"]


def main() -> None:
    from src import app

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--action", choices=action_choices, required=False, default="action1"
    )
    parser.add_argument("--param1", type=str, default="xpto")

    args = parser.parse_args()

    app.run(args.action, args.param1)


if __name__ == "__main__":
    main()
