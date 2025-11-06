"""Report storage implementations following Dependency Inversion Principle."""
from pathlib import Path
from ..interfaces import IReportStorage


class FileStorage(IReportStorage):
    """Store reports to filesystem."""
    
    def __init__(self, base_path: str = ".") -> None:
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)
    
    def save(self, content: str, identifier: str) -> None:
        """Save report content to file."""
        file_path = self.base_path / identifier
        file_path.write_text(content, encoding="utf-8")
        print(f"[FileStorage] Saved to: {file_path}")


class DatabaseStorage(IReportStorage):
    """Store reports to database (simulated)."""
    
    def __init__(self, connection_string: str = "sqlite://reports.db") -> None:
        self.connection_string = connection_string
    
    def save(self, content: str, identifier: str) -> None:
        """Save report content to database."""
        # Simulated database operation
        print(f"[DatabaseStorage] Saved '{identifier}' to {self.connection_string}")
        print(f"[DatabaseStorage] Content length: {len(content)} characters")


class CloudStorage(IReportStorage):
    """Store reports to cloud storage (simulated)."""
    
    def __init__(self, bucket_name: str = "my-reports-bucket") -> None:
        self.bucket_name = bucket_name
    
    def save(self, content: str, identifier: str) -> None:
        """Save report content to cloud storage."""
        # Simulated cloud upload
        print(f"[CloudStorage] Uploaded '{identifier}' to bucket '{self.bucket_name}'")