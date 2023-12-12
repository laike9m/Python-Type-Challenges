import markdown


def render_hints(hints: str) -> str:
    """Render the hints messages to HTML format."""
    return markdown.markdown(hints)
