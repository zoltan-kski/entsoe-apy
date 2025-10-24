#!/usr/bin/env python3
"""Quick test to verify the fixes work."""

from entsoe.config.config import EntsoEConfig, set_log_level
import sys

print("Testing validation and type safety...")
print("=" * 60)

# Test 1: Valid log levels should work
print("\n1. Testing valid log levels:")
try:
    config = EntsoEConfig(log_level="DEBUG")
    print(f"✓ EntsoEConfig(log_level='DEBUG') works: {config.log_level}")
    
    set_log_level("INFO")
    print("✓ set_log_level('INFO') works")
except Exception as e:
    print(f"✗ Failed: {e}")
    sys.exit(1)

# Test 2: Invalid log level should raise ValueError
print("\n2. Testing invalid log level:")
try:
    EntsoEConfig(log_level="INVALID")
    print("✗ Should have raised ValueError!")
    sys.exit(1)
except ValueError as e:
    print(f"✓ Correctly raised ValueError: {e}")

# Test 3: Case insensitive
print("\n3. Testing case insensitive:")
try:
    config = EntsoEConfig(log_level="debug")
    print(f"✓ Case insensitive works: {config.log_level}")
except Exception as e:
    print(f"✗ Failed: {e}")
    sys.exit(1)

# Test 4: Invalid via set_log_level
print("\n4. Testing invalid via set_log_level:")
try:
    set_log_level("INVALID")
    print("✗ Should have raised ValueError!")
    sys.exit(1)
except ValueError as e:
    print(f"✓ Correctly raised ValueError: {e}")

print("\n" + "=" * 60)
print("All tests passed! ✓")
