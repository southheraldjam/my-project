"""Manages the lifecycle of a single overlay session attached (or not)
to a running Crossout client instance.
"""
import logging

logger = logging.getLogger("mod_menu.core.session")


class OverlaySession:
    def __init__(self, process_adapter, overlay_adapter):
        self.process_adapter = process_adapter
        self.overlay_adapter = overlay_adapter
        self._attached = False

    def start(self):
        if self.process_adapter.is_game_running():
            pid = self.process_adapter.attach()
            logger.info("Attached overlay session to pid=%s", pid)
            self.overlay_adapter.initialize(target_pid=pid)
            self._attached = True
        else:
            logger.info("No game process found, overlay running in preview mode")
            self.overlay_adapter.initialize(target_pid=None)
            self._attached = False

    def tick(self):
        if self._attached and not self.process_adapter.is_game_running():
            logger.warning("Game process disappeared, detaching overlay")
            self.stop()
            return
        self.overlay_adapter.render_frame()

    def stop(self):
        self.overlay_adapter.shutdown()
        if self._attached:
            self.process_adapter.detach()
        self._attached = False