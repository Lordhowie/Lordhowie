from dataclasses import dataclass

from typing import Dict, List, Tuple
=======
from typing import List, Tuple


import pandas as pd
from snowflake.snowpark import Session


@dataclass
class Step:
    """Representation of a workflow step."""

    name: str

    function: str
    params: Dict[str, str]


def add_step(steps: List[Step], name: str, function: str, params: Dict[str, str]) -> None:
    """Add a new step to the workflow list."""
    steps.append(Step(name=name, function=function, params=params))
=======
    query: str


def add_step(steps: List[Step], name: str, query: str) -> None:
    """Add a new step to the workflow list."""
    steps.append(Step(name=name, query=query))


def execute_steps(steps: List[Step], session: Session) -> List[Tuple[str, pd.DataFrame]]:
    """Execute each step and return results as (name, DataFrame)."""
    results: List[Tuple[str, pd.DataFrame]] = []
    for step in steps:

        if step.function == "SQL Query":
            query = step.params.get("query", "")
            df = session.sql(query).to_pandas()
            results.append((step.name, df))
        elif step.function == "Run Python":
            code = step.params.get("code", "")
            local_env = {"session": session, "pd": pd}
            exec(code, local_env)
            df = local_env.get("df", pd.DataFrame())
            results.append((step.name, df))
        else:
            # Unknown function - return empty result
            results.append((step.name, pd.DataFrame()))
=======
        df = session.sql(step.query).to_pandas()
        results.append((step.name, df))

    return results
