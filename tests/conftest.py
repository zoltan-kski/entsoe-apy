"""Shared pytest fixtures for all tests."""

import pytest

from entsoe.config.config import logger


@pytest.fixture(autouse=True)
def cleanup_logger():
    """Fixture to clean up logger handlers before and after each test."""
    # Store the initial handler IDs
    initial_handlers = list(logger._core.handlers.keys())

    yield

    # Clean up any handlers added during the test
    current_handlers = list(logger._core.handlers.keys())
    for handler_id in current_handlers:
        if handler_id not in initial_handlers:
            try:
                logger.remove(handler_id)
            except ValueError:
                # Handler may have already been removed; safe to ignore.
                pass
