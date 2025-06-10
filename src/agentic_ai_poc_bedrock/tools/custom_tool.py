from crewai.tools import BaseTool
from typing import Type
import pandas as pd
from pydantic import BaseModel, Field
import pandas as pd
import math
import os
from typing import Optional, List
from crewai.tools import BaseTool
from crewai_tools import RagTool
from pydantic import Field


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
            

class CSVChunkRagTool(BaseTool):
    name: str = "CSV Chunk RAG Tool"
    description: str = "A tool that splits large CSV files into smaller chunks and creates a RAG knowledge base for querying the data."
    
    # Tool configuration
    chunk_size: int = Field(default=500, description="Number of rows per chunk")
    output_dir: str = Field(default="./processed_data", description="Directory to store chunk files")
    rag_config: Optional[dict] = Field(default=None, description="Configuration for RagTool")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._rag_tool = None
        self._setup_rag_tool()
    
    def _setup_rag_tool(self):
        """Initialize the RagTool with custom configuration"""
        default_config = {
            "chunker": {
                "chunk_size": 400,
                "chunk_overlap": 100,
                "length_function": "len",
                "min_chunk_size": 0
            }
        }
        
        # Use provided config or default
        config = self.rag_config if self.rag_config else default_config
        self._rag_tool = RagTool(config=config, summarize=True)
    
    def _split_csv(self, file_path: str) -> List[str]:
        """Split CSV into smaller chunks and return list of chunk file paths"""
        try:
            # Read the CSV file
            df = pd.read_csv(file_path)
            
            # Ensure output directory exists
            os.makedirs(self.output_dir, exist_ok=True)
            
            # Get base filename without extension
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            
            chunk_files = []
            num_chunks = math.ceil(len(df) / self.chunk_size)
            
            # Split into chunks
            for i in range(0, len(df), self.chunk_size):
                chunk = df[i:i + self.chunk_size]
                chunk_num = i // self.chunk_size + 1
                chunk_filename = os.path.join(self.output_dir, f"{base_name}_chunk_{chunk_num}.csv")
                
                # Save chunk
                chunk.to_csv(chunk_filename, index=False)
                chunk_files.append(chunk_filename)
                print(f"Created chunk {chunk_num}/{num_chunks}: {chunk_filename}")
            
            return chunk_files
            
        except Exception as e:
            raise Exception(f"Error splitting CSV file: {str(e)}")
    
    def _add_chunks_to_rag_directory(self) -> str:
        """Add entire directory to RAG tool instead of individual files"""
        try:
            # Use directory approach which is more reliable
            absolute_dir = os.path.abspath(self.output_dir)
            self._rag_tool.add(data_type="directory", path=absolute_dir)
            return f"Successfully added directory {absolute_dir} to RAG knowledge base"
        except Exception as e:
            return f"Error adding directory to RAG: {str(e)}"

    # Then modify your _run method to use this:
    def _run(self, file_path: str, query: Optional[str] = None) -> str:
        try:
            if not os.path.exists(file_path):
                return f"Error: File not found at {file_path}"
            
            # Split CSV into chunks
            print(f"Splitting CSV file: {file_path}")
            chunk_files = self._split_csv(file_path)
            
            # Add entire directory to RAG tool (more reliable)
            print("Adding chunk directory to RAG knowledge base...")
            add_result = self._add_chunks_to_rag_directory()
            
            if query:
                search_result = self._rag_tool._run(query)
                return f"{add_result}\n\nSearch Results:\n{search_result}"
            else:
                return f"{add_result}\n\nRAG knowledge base is ready for queries."
                
        except Exception as e:
            return f"Error processing CSV file: {str(e)}"
            
    def search(self, query: str) -> str:
        """Search the RAG knowledge base"""
        if self._rag_tool is None:
            return "Error: RAG tool not initialized. Please process a CSV file first."
        
        try:
            return self._rag_tool._run(query)
        except Exception as e:
            return f"Error searching knowledge base: {str(e)}"


