from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Function:
    """Available function type in the workflow."""

    name: str
    description: str
    inputs: List[str]


# Built-in function definitions
DEFAULT_FUNCTIONS: Dict[str, Function] = {
    "SQL Query": Function(
        name="SQL Query",
        description="Execute an arbitrary SQL query against Snowflake.",
        inputs=["query"],
    ),
    "Run Python": Function(
        name="Run Python",
        description="Execute Python code in the Snowflake environment. If a variable named 'df' is created it will be shown as the result.",
        inputs=["code"],
    ),
}


def get_default_functions() -> Dict[str, Function]:
    """Return a copy of the default functions."""
    return {name: f for name, f in DEFAULT_FUNCTIONS.items()}


def add_function(functions: Dict[str, Function], name: str, description: str, inputs: List[str]) -> None:
    """Add a user-defined function to the function dictionary."""
    functions[name] = Function(name=name, description=description, inputs=inputs)
