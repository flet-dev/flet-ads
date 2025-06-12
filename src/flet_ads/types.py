from dataclasses import dataclass
from enum import Enum
from typing import Optional

import flet as ft

__all__ = [
    "NativeAdTemplateType",
    "NativeTemplateFontStyle",
    "NativeAdTemplateTextStyle",
    "NativeAdTemplateStyle",
]


class NativeAdTemplateType(Enum):
    SMALL = "small"
    MEDIUM = "medium"


class NativeTemplateFontStyle(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    MONOSPACE = "monospace"


@dataclass
class NativeAdTemplateTextStyle:
    size: ft.OptionalNumber = None
    text_color: ft.OptionalColorValue = None
    bgcolor: ft.OptionalColorValue = None
    style: Optional[NativeTemplateFontStyle] = None


@dataclass
class NativeAdTemplateStyle:
    template_type: NativeAdTemplateType = NativeAdTemplateType.MEDIUM
    main_bgcolor: ft.OptionalColorValue = None
    corner_radius: ft.OptionalNumber = None
    call_to_action_text_style: Optional[NativeAdTemplateTextStyle] = None
    primary_text_style: Optional[NativeAdTemplateTextStyle] = None
    secondary_text_style: Optional[NativeAdTemplateTextStyle] = None
    tertiary_text_style: Optional[NativeAdTemplateTextStyle] = None
