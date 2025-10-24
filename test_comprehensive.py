#!/usr/bin/env python3
"""Comprehensive test of the refactored logger."""

import sys
import pytest
from entsoe.config.config import EntsoEConfig, set_log_level, set_config, get_config

def test_valid_log_levels():
    """Test that all valid log levels work."""
    valid_levels = ["TRACE", "DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"]
    
    for level in valid_levels:
        config = EntsoEConfig(log_level=level)
        assert config.log_level == level
        print(f"✓ {level} works")

def test_case_insensitive():
    """Test case insensitive log levels."""
    config = EntsoEConfig(log_level="debug")
    assert config.log_level == "DEBUG"
    print("✓ Case insensitive works (debug -> DEBUG)")
    
    config = EntsoEConfig(log_level="Success")
    assert config.log_level == "SUCCESS"
    print("✓ Case insensitive works (Success -> SUCCESS)")

def test_invalid_log_level():
    """Test that invalid log level raises ValueError."""
    try:
        EntsoEConfig(log_level="INVALID")  # type: ignore
        print("✗ Should have raised ValueError")
        sys.exit(1)
    except ValueError as e:
        print(f"✓ Invalid log level correctly raises ValueError: {e}")

def test_set_log_level():
    """Test set_log_level function."""
    set_log_level("DEBUG")
    print("✓ set_log_level('DEBUG') works")
    
    try:
        set_log_level("INVALID")  # type: ignore
        print("✗ Should have raised ValueError")
        sys.exit(1)
    except ValueError:
        print("✓ set_log_level with invalid level raises ValueError")

def test_set_config():
    """Test set_config function."""
    set_config(log_level="WARNING")
    config = get_config()
    assert config.log_level == "WARNING"
    print("✓ set_config with log_level works")

def test_default_log_level():
    """Test default log level is SUCCESS."""
    config = EntsoEConfig()
    assert config.log_level == "SUCCESS"
    print("✓ Default log level is SUCCESS")

if __name__ == "__main__":
    print("Running comprehensive logger tests...")
    print("=" * 60)
    
    test_valid_log_levels()
    test_case_insensitive()
    test_invalid_log_level()
    test_set_log_level()
    test_set_config()
    test_default_log_level()
    
    print("=" * 60)
    print("All tests passed! ✓")
