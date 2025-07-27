import flet as ft

from .banner_ad import BannerAd
from .types import NativeAdTemplateStyle

__all__ = ["NativeAd"]


@ft.control("NativeAd")
class NativeAd(BannerAd):
    """
    Renders a native ad.

    Raises:
        AssertionError: When neither [`factory_id`][..] nor
            [`template_style`][..] is set.
    """

    factory_id: str = None
    """
    An identifier for the factory that creates the Platform view.
    """

    template_style: NativeAdTemplateStyle = None
    """
    A style for the native ad template.
    """

    def before_update(self):
        super().before_update()
        assert self.factory_id is not None or self.template_style is not None, (
            "factory_id or template_style must be set"
        )
