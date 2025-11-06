"""Interfaces for the report system following Interface Segregation Principle."""
from abc import ABC, abstractmethod
from typing import Any


class IReportData(ABC):
    """Interface for report data container."""
    
    @abstractmethod
    def get_title(self) -> str:
        """Get the report title."""
        pass
    
    @abstractmethod
    def get_content(self) -> Any:
        """Get the report content."""
        pass


class IReportFormatter(ABC):
    """Interface for formatting report data."""
    
    @abstractmethod
    def format(self, data: IReportData) -> str:
        """Format report data to string representation."""
        pass


class IReportPrinter(ABC):
    """Interface for printing formatted reports."""
    
    @abstractmethod
    def print(self, formatted_content: str) -> None:
        """Print the formatted report."""
        pass


class IReportStorage(ABC):
    """Interface for persisting reports."""
    
    @abstractmethod
    def save(self, content: str, identifier: str) -> None:
        """Save report content."""
        pass