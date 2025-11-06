"""Report formatters following Open/Closed Principle."""
import json
from typing import Any
from ..interfaces import IReportData, IReportFormatter


class PlainTextFormatter(IReportFormatter):
    """Format report as plain text."""
    
    def format(self, data: IReportData) -> str:
        """Format report data as plain text."""
        title = data.get_title()
        content = data.get_content()
        return f"{title}\n{'=' * len(title)}\n{content}"


class JsonFormatter(IReportFormatter):
    """Format report as JSON."""
    
    def format(self, data: IReportData) -> str:
        """Format report data as JSON."""
        return json.dumps({
            "title": data.get_title(),
            "content": data.get_content()
        }, indent=2)


class HtmlFormatter(IReportFormatter):
    """Format report as HTML."""
    
    def format(self, data: IReportData) -> str:
        """Format report data as HTML."""
        title = data.get_title()
        content = data.get_content()
        return f"<html><body><h1>{title}</h1><p>{content}</p></body></html>"


class MarkdownFormatter(IReportFormatter):
    """Format report as Markdown - demonstrates extensibility (O)."""
    
    def format(self, data: IReportData) -> str:
        """Format report data as Markdown."""
        title = data.get_title()
        content = data.get_content()
        return f"# {title}\n\n{content}"