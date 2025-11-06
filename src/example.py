"""Demonstration of SOLID principles in action."""
from solid_report import (
    Report,
    PlainTextFormatter,
    JsonFormatter,
    HtmlFormatter,
    MarkdownFormatter,
    ConsolePrinter,
    GuiPrinter,
    FileStorage,
    DatabaseStorage,
    CloudStorage,
)
from solid_report.interfaces import IReportFormatter, IReportPrinter, IReportStorage


class ReportService:
    """
    High-level service that depends on abstractions (Dependency Inversion).
    This demonstrates the 'D' in SOLID - we depend on interfaces, not concrete classes.
    """
    
    def __init__(
        self,
        formatter: IReportFormatter,
        printer: IReportPrinter,
        storage: IReportStorage,
    ) -> None:
        self.formatter = formatter
        self.printer = printer
        self.storage = storage
    
    def process_report(self, report: Report, save_as: str) -> None:
        """Process a report: format, print, and save."""
        # Format the report
        formatted = self.formatter.format(report)
        
        # Print the report
        self.printer.print(formatted)
        
        # Save the report
        self.storage.save(formatted, save_as)


def main() -> None:
    """Demonstrate SOLID principles with various configurations."""
    
    # Create a report (data model)
    report = Report(
        title="Quarterly Sales Report",
        content="Sales increased by 15% in Q4 2024. Great performance across all regions."
    )
    
    print("=" * 80)
    print("EXAMPLE 1: Plain Text → Console → File")
    print("=" * 80)
    service1 = ReportService(
        formatter=PlainTextFormatter(),
        printer=ConsolePrinter(),
        storage=FileStorage("./reports"),
    )
    service1.process_report(report, "q4_sales.txt")
    
    print("\n" + "=" * 80)
    print("EXAMPLE 2: JSON → GUI → Database")
    print("=" * 80)
    service2 = ReportService(
        formatter=JsonFormatter(),
        printer=GuiPrinter(),
        storage=DatabaseStorage("postgresql://localhost/reports"),
    )
    service2.process_report(report, "q4_sales_json")
    
    print("\n" + "=" * 80)
    print("EXAMPLE 3: HTML → Console → Cloud")
    print("=" * 80)
    service3 = ReportService(
        formatter=HtmlFormatter(),
        printer=ConsolePrinter(),
        storage=CloudStorage("s3://my-company-reports"),
    )
    service3.process_report(report, "q4_sales.html")
    
    print("\n" + "=" * 80)
    print("EXAMPLE 4: Markdown (new format!) → Console → File")
    print("=" * 80)
    # This shows Open/Closed Principle: we can add new formatters without modifying existing code
    service4 = ReportService(
        formatter=MarkdownFormatter(),
        printer=ConsolePrinter(),
        storage=FileStorage("./reports"),
    )
    service4.process_report(report, "q4_sales.md")
    
    print("\n" + "=" * 80)
    print("✓ All examples completed successfully!")
    print("✓ SOLID principles demonstrated:")
    print("  - S: Each class has one responsibility")
    print("  - O: New formatters/printers/storages can be added without modification")
    print("  - L: All implementations are substitutable")
    print("  - I: Interfaces are segregated and specific")
    print("  - D: High-level code depends on abstractions, not concretions")
    print("=" * 80)


if __name__ == "__main__":
    main()