import flet as ft

from .base_ad import BaseAd
from .types import PaidAdEvent


@ft.control("BannerAd")
class BannerAd(BaseAd):
    """
    Displays a banner ad.
    """

    on_will_dismiss: ft.OptionalControlEventCallable = None
    """
    Called before dismissing a full screen view.

    Note:
        Only available on iOS.
    """

    on_paid: ft.OptionalEventCallable[PaidAdEvent] = None
    """
    Called when this ad is estimated to have earned money.

    Available for allowlisted accounts only.
    """
