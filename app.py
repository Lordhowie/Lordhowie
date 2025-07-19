import streamlit as st

from snowflake_utils import create_session
from workflow import Step, add_step, execute_steps

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

# Initialize workflow steps in session state
if "steps" not in st.session_state:
    st.session_state.steps = []

st.header("Add Workflow Step")
with st.form("add_step"):
    name = st.text_input("Step name")
    query = st.text_area("SQL query")
    submitted = st.form_submit_button("Add Step")

if "submitted" in locals() and submitted:
    if query:
        step_name = name or f"Step {len(st.session_state.steps)+1}"
        add_step(st.session_state.steps, step_name, query)
        st.success("Step added")
    else:
        st.warning("Enter a query before adding")

if st.session_state.steps:
    st.subheader("Workflow")
    for i, step in enumerate(st.session_state.steps, 1):
        st.markdown(
            f"<div class='node-box'><div class='node-title'>{i}. {step.name}</div><pre>{step.query}</pre></div>",
            unsafe_allow_html=True,
        )

if st.button("Run Workflow"):
    if not st.session_state.steps:
        st.warning("No steps to run")
    else:
        session = create_session()
        if session:
            results = execute_steps(st.session_state.steps, session)
            for i, (name, df) in enumerate(results, 1):
                st.write(f"Executing {name} ({i})")
                st.dataframe(df)
