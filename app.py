import streamlit as st

from snowflake_utils import create_session
from workflow import Step, add_step, execute_steps
from functions import Function, add_function, get_default_functions

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

# ----- Initialization -----
if "steps" not in st.session_state:
    st.session_state.steps = []

if "functions" not in st.session_state:
    st.session_state.functions = get_default_functions()

page = st.sidebar.radio("Navigate", ("Build Workflow", "Manage Functions"))

# ----- Workflow Builder -----
if page == "Build Workflow":
    st.header("Add Workflow Step")
    function_names = list(st.session_state.functions.keys())
    with st.form("add_step"):
        step_name = st.text_input("Step name")
        selected_function = st.selectbox("Function", function_names)
        params = {}
        for inp in st.session_state.functions[selected_function].inputs:
            if inp.lower() in {"query", "code"}:
                params[inp] = st.text_area(inp)
            else:
                params[inp] = st.text_input(inp)
        submitted = st.form_submit_button("Add Step")
    if submitted:
        name = step_name or f"Step {len(st.session_state.steps)+1}"
        add_step(st.session_state.steps, name, selected_function, params)
        st.success("Step added")

    if st.session_state.steps:
        st.subheader("Workflow")
        for i, step in enumerate(st.session_state.steps, 1):
            st.markdown(
                f"<div class='node-box'><div class='node-title'>{i}. {step.name} - {step.function}</div>"
                + "<pre>" + "\n".join(f"{k}: {v}" for k, v in step.params.items()) + "</pre></div>",
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
                    if not df.empty:
                        st.dataframe(df)

# ----- Manage Functions -----
else:
    st.header("Existing Functions")
    for func in st.session_state.functions.values():
        st.markdown(f"**{func.name}** - {func.description}")
        st.write("Inputs: ", ", ".join(func.inputs) or "None")
    st.divider()

    st.subheader("Add New Function")
    with st.form("add_function"):
        name = st.text_input("Function name")
        description = st.text_area("Description")
        inputs_raw = st.text_input("Input fields (comma separated)")
        submitted = st.form_submit_button("Add Function")
    if submitted:
        inputs = [i.strip() for i in inputs_raw.split(",") if i.strip()]
        if name:
            add_function(st.session_state.functions, name, description, inputs)
            st.success("Function added")
        else:
            st.warning("Function must have a name")
