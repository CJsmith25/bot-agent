#!/usr/bin/env python3
"""
Bot Agent - Main Entry Point

An intelligent automation and interaction bot.
"""

import logging
import asyncio
from bot import BotAgent

def setup_logging():
    """Configure logging for the bot agent."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

async def main():
    """Main entry point for the bot agent."""
    setup_logging()
    logger = logging.getLogger(__name__)
    
    logger.info("Starting Bot Agent...")
    
    # Initialize bot agent
    bot = BotAgent()
    
    try:
        await bot.start()
    except KeyboardInterrupt:
        logger.info("Shutting down Bot Agent...")
    finally:
        await bot.stop()

if __name__ == "__main__":
    asyncio.run(main())
