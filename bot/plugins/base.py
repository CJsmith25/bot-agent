"""
Base Plugin Class

Base class for all bot agent plugins.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any

class BasePlugin(ABC):
    """Base class for bot agent plugins."""
    
    def __init__(self, name: str):
        """Initialize plugin.
        
        Args:
            name: Plugin name
        """
        self.name = name
        self.enabled = False
        
    @abstractmethod
    async def load(self):
        """Load the plugin."""
        pass
        
    @abstractmethod
    async def unload(self):
        """Unload the plugin."""
        pass
        
    @abstractmethod
    async def handle_message(self, message: str) -> str:
        """Handle a message.
        
        Args:
            message: Input message
            
        Returns:
            Response message or None
        """
        pass
