"""Report printers following Liskov Substitution Principle."""
from ..interfaces import IReportPrinter


class ConsolePrinter(IReportPrinter):
    """Print report to console/terminal."""
    
    def print(self, formatted_content: str) -> None:
        """Print formatted content to console."""
        print(formatted_content)


class GuiPrinter(IReportPrinter):
    """Print report in GUI style (simulated)."""
    
    def print(self, formatted_content: str) -> None:
        """Print formatted content with GUI prefix."""
        print(f"[GUI Window]\n{formatted_content}")


class LogPrinter(IReportPrinter):
    """Print report to log output."""
    
    def print(self, formatted_content: str) -> None:
        """Print formatted content as log entry."""
        print(f"[LOG] {formatted_content}")