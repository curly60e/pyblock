"""Safe embedding of user/node text inside Rich markup."""


def safe_markup_text(text: str) -> str:
    """Escape arbitrary text so square brackets are not parsed as markup tags."""
    return text.replace("\\", "\\\\").replace("[", "\\[")