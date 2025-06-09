from crewai.tools import BaseTool
from typing import Type
import pandas as pd
from pydantic import BaseModel, Field
from ironpdf import ChromePdfRenderer

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."

class ReadCSVFileTool(BaseTool):
    name: str = "read_csv_file"
    description: str = "Reads a CSV file from a local path, stores it for downstream tasks, and returns a schema and data profile."

    def _run(self, file_path: str) -> str:
        try:
            df = pd.read_csv(file_path)
            DataStore.set("df", df)
            schema = df.dtypes.to_string()
            profile = df.describe(include='all').to_string()
            return f"✅ CSV Loaded Successfully\n\n📄 Schema:\n{schema}\n\n📊 Profile:\n{profile}"
        except Exception as e:
            return f"❌ Failed to read CSV: {str(e)}"

class PDFConverterTool(BaseTool):
    name: str = "convert_to_pdf"
    description: str = "Reads a markdown file and converts to PDF."

    def _run(self, file_path: str) -> str:
        try:
            renderer = ChromePdfRenderer()
            pdf = renderer.RenderMarkdownFileAsPdf(file_path + ".md")
            pdf.SaveAs(file_path + ".pdf")
            return "File converted to pdf"
        except Exception as e:
            return f"❌ Failed to convert to PDF: {str(e)}"

