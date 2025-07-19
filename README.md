# Streamlit Snowflake n8n App

This project contains a small Streamlit application meant to run in
Snowflake's Streamlit environment. The UI is inspired by `n8n` and lets
you define workflows made up of **Functions** such as SQL queries or
Python code. Functions can be managed on a dedicated page and each step
in the workflow selects one of these functions and supplies the required
inputs.

The code has been split into helper modules to keep the main app file
concise:

- `snowflake_utils.py` – creates a Snowflake `Session`
- `workflow.py` – stores workflow and execution logic
- `functions.py` – manages available function types
=======
This project contains a minimal Streamlit application meant to run in
Snowflake's Streamlit environment. The app lets you build a list of SQL
steps and execute them sequentially with a simple UI inspired by `n8n`.

 <<<<<<< rcnrdz-codex/create-streamlit-app-in-snowflake-with-n8-functionality
The code has been split into small helper modules to keep the main app
file concise:

- `snowflake_utils.py` – creates a Snowflake `Session`
- `workflow.py` – stores workflow step logic




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


Use the **Manage Functions** page to add new function types with a name,
description and list of input fields. The **Build Workflow** page lets
you add workflow steps by selecting a function and filling in its
inputs, then execute the steps sequentially against Snowflake.
=======
The app will allow you to add SQL queries as workflow steps and run them
in order against your Snowflake database.

