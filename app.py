import streamlit as st
from snowflake_helper import create_session
import workflow

st.set_page_config(page_title="Snowflake n8n Workflow", page_icon=":snowflake:")
st.title("Snowflake Streamlit App - n8n")

st.markdown(
    """
    <style>
        .node-box {
            border: 1px solid #ddd;
            border-radius: 6px;
            padding: 0.5rem;
            margin-bottom: 0.5rem;
            background-color: #fafafa;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }
        .node-title {
            font-weight: 600;
            color: #228b22;
            margin-bottom: 0.25rem;
        }
        pre {
            margin: 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

workflow.init_state()

st.header("Add Workflow Step")
with st.form("add_step"):
    name = st.text_input("Step name")
    query = st.text_area("SQL query")
    submitted = st.form_submit_button("Add Step")

if 'submitted' in locals() and submitted:
    if workflow.add_step(name, query):
        st.success("Step added")
    else:
        st.warning("Enter a query before adding")

if st.session_state.steps:
    workflow.render_steps()

if st.button("Run Workflow"):
    if not st.session_state.steps:
        st.warning("No steps to run")
    else:
        session = create_session()
        if session:
            for i, step in enumerate(st.session_state.steps, 1):
                st.write(f"Executing {step.name} ({i})")
                df = session.sql(step.query).to_pandas()
                st.dataframe(df)
