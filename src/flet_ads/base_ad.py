from dataclasses import field

import flet as ft

from flet_ads.types import AdRequest


@ft.control
class BaseAd(ft.Control):
    """
    Base class for all ad controls in Flet Ads package.

    Raises:
        AssertionError: When using this control on a web and/or non-mobile platform.
    """

    unit_id: str
    """
    Ad unit ID for this ad.
    """

    request: AdRequest = field(default_factory=lambda: AdRequest())
    """
    Targeting information used to fetch an Ad.
    """

    on_load: ft.OptionalControlEventHandler["BaseAd"] = None
    """
    Called when this ad is loaded successfully.
    """

    on_error: ft.OptionalControlEventHandler["BaseAd"] = None
    """
    Called when an ad request failed.
    
    Event handler argument `data` property contains information about the error.
    """

    on_open: ft.OptionalControlEventHandler["BaseAd"] = None
    """
    Called when this ad opens up.
    
    A full screen view/overlay is presented in response to the user clicking
    on an ad. You may want to pause animations and time sensitive
    interactions.
    """

    on_close: ft.OptionalControlEventHandler["BaseAd"] = None
    """
    Called when the full screen view has been closed. You should restart
    anything paused while handling [`on_open`][..].
    """

    on_impression: ft.OptionalControlEventHandler["BaseAd"] = None
    """
    Called when an impression occurs on this ad.
    """

    on_click: ft.OptionalControlEventHandler["BaseAd"] = None
    """
    Called when this ad is clicked.
    """

    def before_update(self):
        assert (
            not self.page.web and self.page.platform.is_mobile()
        ), f"{self.__class__.__name__} is only supported on Mobile (Android and iOS)"
