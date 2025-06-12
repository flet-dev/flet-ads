import flet as ft

from .base_ad import BaseAd
from .types import NativeAdTemplateStyle

__all__ = ["NativeAd"]


@ft.control("NativeAd")
class NativeAd(BaseAd):
    """
    TBA
    """

    factory_id: str = None
    """
    
    """

    template_style: NativeAdTemplateStyle = None
    """
    
    """

    def before_update(self):
        super().before_update()
        assert (
            self.factory_id or self.template_style
        ), "factory_id or template_style must be set"
