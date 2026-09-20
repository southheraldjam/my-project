"""Thin handler that turns UI/hotkey actions into calls against the
services layer. No direct platform or persistence code lives here.
"""
import logging

from models.mod_profile import ModProfile

logger = logging.getLogger("mod_menu.handlers.ui_command")


class UICommandHandler:
    def