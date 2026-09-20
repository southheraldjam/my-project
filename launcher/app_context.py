"""Application-wide composition root.

Builds and holds references to the adapters and services so the rest of
the app doesn't need to know how objects are constructed.
"""
from dataclasses import dataclass

from adapters.windows.overlay_adapter import OverlayAdapter
from adapters.windows.process_adapter import ProcessAdapter
from config.settings import Settings
from services.loadout_service import LoadoutService
from services.profile_service import ProfileService
from services.update_service import UpdateService


@dataclass
class AppContext:
    settings: Settings
    process_adapter: ProcessAdapter
    overlay_adapter: OverlayAdapter
    profile_service: ProfileService
    loadout_service: LoadoutService
    update_service: UpdateService

    @classmethod
    def create(cls, settings: Settings) -> "AppContext":
        process_adapter = ProcessAdapter(process_name=settings.game_process_name)
        overlay_adapter = OverlayAdapter(native_module_path=settings.native_module_path)

        profile_service = ProfileService(storage_path=settings.profiles_path)
        loadout_service = LoadoutService(storage_path=settings.loadouts_path)
        update_service = UpdateService(
            update_url=settings.update_endpoint,
            current_version=settings.app_version,
        )

        return cls(
            settings=settings,
            process_adapter=process_adapter,
            overlay_adapter=overlay_adapter,
            profile_service=profile_service,
            loadout_service=loadout_service,
            update_service=update_service,
        )