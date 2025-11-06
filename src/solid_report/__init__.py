"""SOLID Report - A demonstration of SOLID principles in Python."""

from .models import Report
from .formatters import (
    PlainTextFormatter,
    JsonFormatter,
    HtmlFormatter,
    MarkdownFormatter,
)
from .printers import ConsolePrinter, GuiPrinter, LogPrinter
from .storage import FileStorage, DatabaseStorage, CloudStorage

__version__ = "0.1.0"

__all__ = [
    "Report",
    "PlainTextFormatter",
    "JsonFormatter",
    "HtmlFormatter",
    "MarkdownFormatter",
    "ConsolePrinter",
    "GuiPrinter",
    "LogPrinter",
    "FileStorage",
    "DatabaseStorage",
    "CloudStorage",
]