#!/usr/bin/env python
import sys
import warnings
import os

from datetime import datetime

from agentic_ai_poc_bedrock.crew import AgenticAiPocBedrock

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=SyntaxWarning, module="alembic")
# Suppress the specific warning at the start of your script
warnings.filterwarnings(
    "ignore",
    message=".*Accessing the 'model_fields' attribute on the instance is deprecated.*",
    category=DeprecationWarning
)
warnings.filterwarnings(
    "ignore",
    message=".*Consider adding path_separator=os to Alembic config.*",
    category=DeprecationWarning
)

# Disable CrewAI telemetry only
os.environ['CREWAI_DISABLE_TELEMETRY'] = 'true'

# Disable all OpenTelemetry (including CrewAI)
os.environ['OTEL_SDK_DISABLED'] = 'true'

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        "topic": "Customer Churn",
        "file_path": "./data/Bank_Customer_Churn_Prediction.csv",
        'current_year': str(datetime.now().year)
    }
    
    try:
        print(f"Current working directory: {os.getcwd()}")
        AgenticAiPocBedrock().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Customer Churn",
        'current_year': str(datetime.now().year)
    }
    try:
        AgenticAiPocBedrock().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AgenticAiPocBedrock().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "Customer Churn",
        "current_year": str(datetime.now().year)
    }
    
    try:
        AgenticAiPocBedrock().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
        
