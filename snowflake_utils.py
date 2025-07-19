import os
import streamlit as st
from snowflake.snowpark import Session


def create_session():
    """Create a Snowflake session from environment variables."""
    conn_params = {
        "account": os.environ.get("SNOWFLAKE_ACCOUNT"),
        "user": os.environ.get("SNOWFLAKE_USER"),
        "password": os.environ.get("SNOWFLAKE_PASSWORD"),
        "role": os.environ.get("SNOWFLAKE_ROLE"),
        "warehouse": os.environ.get("SNOWFLAKE_WAREHOUSE"),
        "database": os.environ.get("SNOWFLAKE_DATABASE"),
        "schema": os.environ.get("SNOWFLAKE_SCHEMA"),
    }
    if not all(conn_params.values()):
        missing = [k for k, v in conn_params.items() if not v]
        st.warning(f"Missing connection parameters: {', '.join(missing)}")
        return None
    return Session.builder.configs(conn_params).create()
