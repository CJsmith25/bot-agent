"""
Plugin System

Manages bot agent plugins and extensions.
"""

from .manager import PluginManager
from .base import BasePlugin

__all__ = ["PluginManager", "BasePlugin"]
