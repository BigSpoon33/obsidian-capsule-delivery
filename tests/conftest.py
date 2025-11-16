"""Pytest configuration and fixtures for capsule tests"""

import pytest
from pathlib import Path
import tempfile


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing"""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


# Additional fixtures will be added in Epic 13
