import asyncio

import flet as ft

from .base_ad import BaseAd


@ft.control("InterstitialAd")
class InterstitialAd(BaseAd):
    """
    Displays a full-screen interstitial ad.
    """

    def show(self):
        asyncio.create_task(self.show_async())

    async def show_async(self):
        await self._invoke_method_async("show")
