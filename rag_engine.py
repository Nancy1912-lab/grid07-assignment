# checking if prompt is safe

blocked_words = [
    "ignore previous instructions",
    "reveal system prompt",
    "delete memory",
    "bypass security"
]blocked_words = [
    "ignore previous instructions",
    "reveal system prompt",
    "delete memory",
    "bypass security"
]


def check_prompt(user_input):

    lower_text = user_input.lower()

    for word in blocked_words:

        if word in lower_text:

            return False

    return True
