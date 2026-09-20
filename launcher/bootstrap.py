"""Entry point for the Crossout Mod Menu desktop application.

Responsible for wiring together configuration, logging, the platform
adapters and the core menu engine before handing off control to the UI
event loop. Keep this module thin - all real logic lives in core/,
services/ and handlers/.
"""
import argparse
import sys

from config.settings import load_settings
from core.menu_engine import MenuEngine
from launcher.app_context import AppContext
from utils.logger import configure_logging


def parse_args(argv):
    parser = argparse.ArgumentParser(prog="crossout-mod-menu")
    parser.add_argument("--dev", action="store_true", help="run in developer mode")
    parser.add_argument("--profile", default=None, help="profile to load on startup")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    configure_logging(dev_mode=args.dev)

    settings = load_settings(dev_mode=args.dev)
    context = AppContext.create(settings=settings)

    engine = MenuEngine(context=context)
    engine.startup(initial_profile=args.profile)

    try:
        return engine.run_forever()
    finally:
        engine.shutdown()


if __name__ == "__main__":
    raise SystemExit(main())