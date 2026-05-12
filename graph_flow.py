from rag_engine import check_prompt
from typing import TypedDict

from langgraph.graph import StateGraph, END

from router import find_best_persona


class GraphState(TypedDict):
    topic: str
    persona: str
    response: str


def select_persona(state):

    result = find_best_persona(state["topic"])

    state["persona"] = result["name"]

    return state


def generate_response(state):

    topic = state["topic"]
    persona = state["persona"]

    is_safe = check_prompt(topic)

    if not is_safe:

        state["response"] = "Unsafe prompt detected."

        return state

    text = f"""
    Persona Selected: {persona}

    Generated Content:
    Here is a simple post about {topic}.
    """

    state["response"] = text

    return state


builder = StateGraph(GraphState)

builder.add_node("persona_selector", select_persona)

builder.add_node("response_generator", generate_response)

builder.set_entry_point("persona_selector")

builder.add_edge("persona_selector", "response_generator")

builder.add_edge("response_generator", END)

graph = builder.compile()