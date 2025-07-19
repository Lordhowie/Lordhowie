from dataclasses import dataclass
from typing import List, Tuple

import pandas as pd
from snowflake.snowpark import Session


@dataclass
class Step:
    """Representation of a workflow step."""

    name: str
    query: str


def add_step(steps: List[Step], name: str, query: str) -> None:
    """Add a new step to the workflow list."""
    steps.append(Step(name=name, query=query))


def execute_steps(steps: List[Step], session: Session) -> List[Tuple[str, pd.DataFrame]]:
    """Execute each step and return results as (name, DataFrame)."""
    results: List[Tuple[str, pd.DataFrame]] = []
    for step in steps:
        df = session.sql(step.query).to_pandas()
        results.append((step.name, df))
    return results
