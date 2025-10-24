#!/usr/bin/env python3
"""Quick test to verify the simplified logger works correctly."""

from entsoe.config.config import logger, set_log_level

print("Testing simplified independent logger")
print("=" * 60)

# Test 1: Default level is SUCCESS
print("\n1. Testing default SUCCESS level:")
logger.info("This INFO should NOT appear")
logger.success("This SUCCESS should appear")
logger.warning("This WARNING should appear")

# Test 2: Change to DEBUG
print("\n2. Changing to DEBUG level:")
set_log_level("DEBUG")
logger.debug("This DEBUG should now appear")
logger.info("This INFO should now appear")

# Test 3: Change to WARNING
print("\n3. Changing to WARNING level:")
set_log_level("WARNING")
logger.info("This INFO should NOT appear")
logger.success("This SUCCESS should NOT appear")
logger.warning("This WARNING should appear")

print("\n" + "=" * 60)
print("All tests completed successfully!")
