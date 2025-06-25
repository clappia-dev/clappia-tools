"""
Clappia Tools - LangChain integration for Clappia API

This package provides a unified client for interacting with Clappia APIs.
"""

from .client.clappia_client import ClappiaClient

__version__ = "0.1.0"
__all__ = ["ClappiaClient"]


def __dir__():
    return __all__
