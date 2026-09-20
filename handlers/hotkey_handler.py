"""Thin handler that translates global keyboard events into engine
actions. Contains no business logic - it only maps key combos to
action identifiers.
"""
import logging
from typing import Callable

import keyboard

from models.hotkey_binding import HotkeyBinding

logger = logging.getLogger("mod_menu.handlers.hotkey")

DEFAULT_BINDINGS = [
    HotkeyBinding(key_combo="f1", action_id="menu.toggle_visibility"),
    HotkeyBinding(key_combo="f2", action_id="profile.cycle_next"),
    HotkeyBinding(key_combo="f3", action_id="loadout.apply_selected"),
    HotkeyBinding(key_combo="ctrl+f9", action_id="menu.panic_close"),
]


class HotkeyHandler:
    def __init__(self, on_action: Callable[[str, dict | None], None]):
        self._on_action = on_action
        self._bindings: list[HotkeyBinding] = []

    def register_defaults(self):
        for binding in DEFAULT_BINDINGS:
            self.register(binding)

    def register(self, binding: HotkeyBinding):
        if not binding.enabled:
            return
        keyboard.add_hotkey(
            binding.key_combo,
            lambda b=binding: self._on_action(b.action_id, None),
        )
        self._bindings.append(binding)
        logger.debug("Registered hotkey %s -> %s", binding.key_combo, binding.action_id)

    def unregister_all(self):
        keyboard.unhook_all_hotkeys()
        self._bindings.clear()