"""Capsule data model - represents a packaged collection of Obsidian content."""

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Optional


@dataclass
class Capsule:
    """
    Represents a capsule - a packaged collection of educational content.

    A capsule is the core entity for content distribution in OCDS.
    It contains metadata, file references, and configuration.

    Attributes:
        capsule_id: Unique identifier (e.g., "TCM_Herbs_v1")
        name: Human-readable name (e.g., "TCM Materia Medica - Herbs")
        version: Semantic version string (e.g., "1.0.0")
        domain_type: Content domain (e.g., "tcm", "education", "reference")
        description: Optional capsule description
        author: Optional author name
        created: ISO 8601 creation timestamp
        updated: ISO 8601 last updated timestamp

    Example:
        >>> cap = Capsule(
        ...     capsule_id="test-v1",
        ...     name="Test Capsule",
        ...     version="1.0.0",
        ...     domain_type="education"
        ... )
        >>> cap.capsule_id
        'test-v1'
    """

    # Required fields
    capsule_id: str
    name: str
    version: str
    domain_type: str

    # Optional fields with defaults
    description: Optional[str] = None
    author: Optional[str] = None
    created: Optional[str] = None
    updated: Optional[str] = None

    def __post_init__(self) -> None:
        """Initialize timestamps if not provided."""
        if self.created is None:
            self.created = self._now_iso()
        if self.updated is None:
            self.updated = self._now_iso()

    @staticmethod
    def _now_iso() -> str:
        """Get current time in ISO 8601 format (UTC)."""
        return datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> dict:
        """
        Serialize capsule to dictionary.

        Returns:
            Dictionary representation of the capsule

        Example:
            >>> cap = Capsule(capsule_id="test-v1", name="Test",
            ...               version="1.0.0", domain_type="education")
            >>> data = cap.to_dict()
            >>> data["capsule_id"]
            'test-v1'
        """
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Capsule":
        """
        Create capsule from dictionary.

        Args:
            data: Dictionary with capsule fields

        Returns:
            Capsule instance

        Example:
            >>> data = {
            ...     "capsule_id": "test-v1",
            ...     "name": "Test",
            ...     "version": "1.0.0",
            ...     "domain_type": "education"
            ... }
            >>> cap = Capsule.from_dict(data)
            >>> cap.name
            'Test'
        """
        return cls(**data)
