"""
Configuration Management

Handles bot agent configuration and settings.
"""

import json
import os
from typing import Dict, Any, Optional

class Config:
    """Configuration manager for bot agent."""
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize configuration.
        
        Args:
            config_path: Path to configuration file
        """
        self.config_path = config_path or "config.json"
        self.settings = self._load_config()
        
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file.
        
        Returns:
            Configuration dictionary
        """
        default_config = {
            "bot": {
                "name": "Bot Agent",
                "version": "0.1.0",
                "debug": False
            },
            "plugins": {
                "enabled": []
            },
            "api": {
                "rate_limit": 100,
                "timeout": 30
            }
        }
        
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r') as f:
                    user_config = json.load(f)
                # Merge user config with defaults
                default_config.update(user_config)
            except Exception as e:
                print(f"Warning: Could not load config file: {e}")
                
        return default_config
        
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value.
        
        Args:
            key: Configuration key (supports dot notation)
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        keys = key.split('.')
        value = self.settings
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
                
        return value
