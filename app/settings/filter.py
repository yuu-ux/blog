from datetime import datetime
from markdown import markdown
from markupsafe import Markup


def setup_filter(app):
    app.jinja_env.filters['format_date'] = format_date
    app.jinja_env.filters['markdown'] = markdown_filter


def format_date(value):
    if isinstance(value, datetime):
        return value.strftime('%Y-%m-%d')
    return value


def markdown_filter(text):
    return Markup(markdown(text))
