import flet as ft

from .base_ad import BaseAd
from .types import PaidAdEvent


@ft.control("BannerAd")
class BannerAd(BaseAd):
    """
    Displays a banner ad.

    Raises:
        AssertionError: When using this control on a web and/or non-mobile platform.
    """

    on_will_dismiss: ft.OptionalControlEventHandler["BannerAd"] = None
    """
    Called before dismissing a full screen view.

    Note:
        Only available on iOS.
    """

    on_paid: ft.OptionalControlEventHandler[PaidAdEvent["BannerAd"]] = None
    """
    Called when this ad is estimated to have earned money.

    Available for allowlisted accounts only.
    """
