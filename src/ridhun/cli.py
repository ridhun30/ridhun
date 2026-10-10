import argparse

from ridhun import __version__
from ridhun.core import greet


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ridhun", description="Say hello.")
    parser.add_argument("name", nargs="?", default="world", help="who to greet")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args(argv)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
