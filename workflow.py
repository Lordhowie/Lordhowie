from dataclasses import dataclass
import streamlit as st


@dataclass
class Step:
    name: str
    query: str


def init_state():
    """Ensure the Streamlit session state contains a steps list."""
    if "steps" not in st.session_state:
        st.session_state.steps = []


def add_step(name: str, query: str) -> bool:
    """Add a new workflow step. Returns True if added."""
    if not query:
        return False
    if not name:
        name = f"Step {len(st.session_state.steps) + 1}"
    st.session_state.steps.append(Step(name, query))
    return True


def render_steps():
    """Render all steps in n8n-style boxes."""
    st.subheader("Workflow")
    for i, step in enumerate(st.session_state.steps, 1):
        st.markdown(
            f"<div class='node-box'><div class='node-title'>{i}. {step.name}</div><pre>{step.query}</pre></div>",
            unsafe_allow_html=True,
        )
