import flet as ft


@ft.control
class BaseAd(ft.Control):
    unit_id: str
    on_load: ft.OptionalControlEventCallable = None
    on_error: ft.OptionalControlEventCallable = None
    on_open: ft.OptionalControlEventCallable = None
    on_close: ft.OptionalControlEventCallable = None
    on_impression: ft.OptionalControlEventCallable = None
    on_click: ft.OptionalControlEventCallable = None
    on_will_dismiss: ft.OptionalControlEventCallable = None

    def before_update(self):
        assert (
            not self.page.web and self.page.platform.is_mobile()
        ), f"{self.__class__.__name__} is only supported on Mobile (Android and iOS)"
