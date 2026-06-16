"""
Plugin Manager

Handles loading, unloading, and managing bot plugins.
"""

import logging
import importlib
from typing import Dict, List
from .base import BasePlugin

class PluginManager:
    """Manages bot agent plugins."""
    
    def __init__(self):
        """Initialize plugin manager."""
        self.logger = logging.getLogger(__name__)
        self.plugins: Dict[str, BasePlugin] = {}
        
    async def load_plugins(self):
        """Load all enabled plugins."""
        self.logger.info("Loading plugins...")
        # TODO: Implement plugin loading from config
        
    async def unload_plugins(self):
        """Unload all plugins."""
        self.logger.info("Unloading plugins...")
        for plugin in self.plugins.values():
            await plugin.unload()
        self.plugins.clear()
        
    async def register_plugin(self, plugin: BasePlugin):
        """Register a plugin.
        
        Args:
            plugin: Plugin instance to register
        """
        self.plugins[plugin.name] = plugin
        await plugin.load()
        self.logger.info(f"Registered plugin: {plugin.name}")
