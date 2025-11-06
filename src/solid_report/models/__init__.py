"""Report data models following Single Responsibility Principle."""
from typing import Any
from ..interfaces import IReportData


class Report(IReportData):
    """Simple report data container - only responsible for holding data."""
    
    def __init__(self, title: str, content: Any) -> None:
        self._title = title
        self._content = content
    
    def get_title(self) -> str:
        """Get the report title."""
        return self._title
    
    def get_content(self) -> Any:
        """Get the report content."""
        return self._content