"""Test module for verifying debug logging functionality."""

from unittest.mock import Mock, patch

import pytest

from entsoe.config import get_config
from entsoe.query.query_api import query_core
from entsoe.utils.utils import check_date_range_limit, split_date_range



class TestLogging:
    """Test class for logging functionality."""

    def test_utility_functions_have_logging(self):
        """Test that utility functions can be called and log debug messages."""
        # Test check_date_range_limit
        with patch("entsoe.utils.utils.logger") as mock_logger:
            check_date_range_limit(202301010000, 202301020000, 365)
            assert mock_logger.debug.called
            # Verify that logging calls mention the function purpose
            call_args = [call[0][0] for call in mock_logger.debug.call_args_list]
            assert any("Checking date range limit" in arg for arg in call_args)

    def test_split_date_range_logging(self):
        """Test that split_date_range logs debug messages."""
        with patch("entsoe.utils.utils.logger") as mock_logger:
            split_date_range(202301010000, 202301050000)
            assert mock_logger.debug.called
            # Verify that logging calls mention the function purpose
            call_args = [call[0][0] for call in mock_logger.debug.call_args_list]
            assert any("Splitting date range" in arg for arg in call_args)
