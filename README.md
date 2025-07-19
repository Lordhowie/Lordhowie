# Streamlit Snowflake n8n App

This project contains a minimal Streamlit application meant to run in
Snowflake's Streamlit environment. The app lets you build a list of SQL
steps and execute them sequentially with a simple UI inspired by `n8n`.

## Running locally

Install the required packages:

```bash
pip install streamlit snowflake-snowpark-python
```

Set your Snowflake credentials via environment variables:

- `SNOWFLAKE_ACCOUNT`
- `SNOWFLAKE_USER`
- `SNOWFLAKE_PASSWORD`
- `SNOWFLAKE_ROLE`
- `SNOWFLAKE_WAREHOUSE`
- `SNOWFLAKE_DATABASE`
- `SNOWFLAKE_SCHEMA`

Then start the app:

```bash
streamlit run app.py
```

The app will allow you to add SQL queries as workflow steps and run them
in order against your Snowflake database.
