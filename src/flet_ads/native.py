import dataclasses
from enum import Enum
from typing import Optional

import flet as ft

from .base_ad import BaseAd

__all__ = [
    "NativeAd",
    "NativeAdTemplateStyle",
    "NativeAdTemplateTextStyle",
    "NativeAdTemplateType",
]


class NativeAdTemplateType(Enum):
    SMALL = "small"
    MEDIUM = "medium"


class NativeTemplateFontStyle(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    MONOSPACE = "monospace"


@dataclasses.dataclass
class NativeAdTemplateTextStyle:
    size: ft.OptionalNumber = None
    text_color: ft.OptionalColorValue = None
    bgcolor: ft.OptionalColorValue = None
    style: Optional[NativeTemplateFontStyle] = None


@dataclasses.dataclass
class NativeAdTemplateStyle:
    template_type: NativeAdTemplateType = NativeAdTemplateType.MEDIUM
    main_bgcolor: ft.OptionalColorValue = None
    corner_radius: ft.OptionalNumber = None
    call_to_action_text_style: Optional[NativeAdTemplateTextStyle] = None
    primary_text_style: Optional[NativeAdTemplateTextStyle] = None
    secondary_text_style: Optional[NativeAdTemplateTextStyle] = None
    tertiary_text_style: Optional[NativeAdTemplateTextStyle] = None


@ft.control("NativeAd")
class NativeAd(BaseAd):
    """
    TBA

    -----

    Online docs: https://flet.dev/docs/controls/nativead
    """

    factory_id: str = None
    template_style: NativeAdTemplateStyle = None

    def before_update(self):
        super().before_update()
        assert (
            self.factory_id or self.template_style
        ), "factory_id or template_style must be set"
