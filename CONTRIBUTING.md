# Contributing to my-project (Crossout Mod Menu)

Thanks for your interest in improving this project. `my-project` is a Windows
desktop companion application that provides a configurable overlay menu,
profile management and loadout presets for Crossout players.

## Ground rules

- All changes must go through a pull request against `develop`.
- Keep platform adapters (`adapters/windows`, `adapters/native`) isolated from
  business logic in `services/` and `models/`. Handlers should stay thin and
  simply translate UI/input events into service calls.
- Any code that talks to the game process must go through
  `adapters/windows/process_adapter.py`. Do not call WinAPI directly from
  services or handlers.
- New features that touch native code (`adapters/native/*`) require a review
  from a maintainer familiar with the C++ side.

## Development setup

1. Install Python 3.11+ for Windows.
2. `pip install -r requirements.txt`
3. Run the app in dev mode: `python -m launcher.bootstrap --dev`
4. Run tests: `pytest tests/`

## Commit style

- Use conventional prefixes: `feat:`, `fix:`, `chore:`, `refactor:`, `test:`.
- Reference the affected layer in the message, e.g. `feat(services): add
  loadout duplication`.

## Reporting issues

Please include your `logs/mod-menu.log` output (with any personal paths
redacted) and the exact Crossout client build you were running against.