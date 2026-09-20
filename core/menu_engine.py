"""Core orchestration for the mod menu.

MenuEngine ties handlers to services and owns the top level lifecycle of
an overlay session. It intentionally contains no platform-specific code -
that belongs in adapters/.
"""
import logging
import time

from core.overlay_session import OverlaySession
from handlers.hotkey_handler import HotkeyHandler
from handlers.ui_command_handler import UICommandHandler

logger = logging.getLogger("mod_menu.core.engine")


class MenuEngine:
    def __init__(self, context):
        self.context = context
        self.session: OverlaySession | None = None
        self.hotkey_handler = HotkeyHandler(on_action=self.handle_action)
        self.ui_handler = UICommandHandler(
            profile_service=context.profile_service,
            loadout_service=context.loadout_service,
        )
        self._running = False

    def startup(self, initial_profile: str | None = None):
        logger.info("Starting mod menu engine")
        self.hotkey_handler.register_defaults()

        if not self.context.process_adapter.is_game_running():
            logger.warning("Crossout process not detected, running in standalone mode")

        self.session = OverlaySession(
            process_adapter=self.context.process_adapter,
            overlay_adapter=self.context.overlay_adapter,
        )
        self.session.start()

        profile_name = initial_profile or self.context.settings.default_profile
        profile = self.context.profile_service.get_profile(profile_name)
        if profile:
            self.ui_handler.apply_profile(profile)

        self._running = True

    def handle_action(self, action_id: str, payload: dict | None = None):
        logger.debug("Dispatching action %s payload=%s", action_id, payload)
        self.ui_handler.dispatch(action_id, payload or {})

    def run_forever(self) -> int:
        try:
            while self._running:
                self.session.tick()
                time.sleep(1 / 30)
        except KeyboardInterrupt:
            logger.info("Interrupted by user")
        return 0

    def shutdown(self):
        logger.info("Shutting down mod menu engine")
        self._running = False
        self.hotkey_handler.unregister_all()
        if self.session:
            self.session.stop()