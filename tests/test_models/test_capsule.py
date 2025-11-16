"""Tests for Capsule model."""

import pytest

from capsule.models.capsule import Capsule


def test_capsule_creation() -> None:
    """Test basic capsule instantiation."""
    cap = Capsule(
        capsule_id="test-capsule-v1",
        name="Test Capsule",
        version="1.0.0",
        domain_type="education",
    )

    assert cap.capsule_id == "test-capsule-v1"
    assert cap.name == "Test Capsule"
    assert cap.version == "1.0.0"
    assert cap.domain_type == "education"


def test_capsule_required_fields() -> None:
    """Test that all required fields must be provided."""
    # This should work
    cap = Capsule(
        capsule_id="required-test",
        name="Required Test",
        version="1.0.0",
        domain_type="test",
    )
    assert cap.capsule_id == "required-test"

    # Missing required field should raise TypeError
    with pytest.raises(TypeError):
        Capsule(name="Missing ID", version="1.0.0", domain_type="test")  
# type: ignore


def test_capsule_optional_fields() -> None:
    """Test optional fields work correctly."""
    cap = Capsule(
        capsule_id="optional-test",
        name="Optional Test",
        version="1.0.0",
        domain_type="test",
        description="Test description",
        author="Test Author",
    )

    assert cap.description == "Test description"
    assert cap.author == "Test Author"


def test_capsule_timestamps_auto_generated() -> None:
    """Test that timestamps are auto-generated if not provided."""
    cap = Capsule(
        capsule_id="timestamp-test",
        name="Timestamp Test",
        version="1.0.0",
        domain_type="test",
    )

    assert cap.created is not None
    assert cap.updated is not None
    assert "T" in cap.created  # ISO 8601 format includes 'T'
    assert "Z" in cap.created or "+" in cap.created  # Timezone indicator


def test_capsule_to_dict() -> None:
    """Test serialization to dictionary."""
    cap = Capsule(
        capsule_id="dict-test",
        name="Dict Test",
        version="1.0.0",
        domain_type="test",
    )

    cap_dict = cap.to_dict()

    assert isinstance(cap_dict, dict)
    assert cap_dict["capsule_id"] == "dict-test"
    assert cap_dict["name"] == "Dict Test"
    assert cap_dict["version"] == "1.0.0"
    assert cap_dict["domain_type"] == "test"


def test_capsule_from_dict() -> None:
    """Test deserialization from dictionary."""
    data = {
        "capsule_id": "from-dict-test",
        "name": "From Dict Test",
        "version": "2.0.0",
        "domain_type": "reference",
        "description": "Test description",
    }

    cap = Capsule.from_dict(data)

    assert cap.capsule_id == "from-dict-test"
    assert cap.name == "From Dict Test"
    assert cap.version == "2.0.0"
    assert cap.domain_type == "reference"
    assert cap.description == "Test description"


def test_capsule_roundtrip() -> None:
    """Test that to_dict() and from_dict() are inverses."""
    original = Capsule(
        capsule_id="roundtrip-test",
        name="Roundtrip Test",
        version="3.0.0",
        domain_type="education",
        author="Test Author",
    )

    # Serialize and deserialize
    data = original.to_dict()
    restored = Capsule.from_dict(data)

    # Should be equal
    assert restored.capsule_id == original.capsule_id
    assert restored.name == original.name
    assert restored.version == original.version
    assert restored.domain_type == original.domain_type
    assert restored.author == original.author
# flake8: noqa: F821
