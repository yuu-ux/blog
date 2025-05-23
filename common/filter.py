from datetime import datetime
from markdown import markdown
from markupsafe import Markup
import bleach
from urllib.parse import urlparse
from bleach.linkifier import Linker


def setup_filter(app):
    app.jinja_env.filters['format_date'] = format_date
    app.jinja_env.filters['markdown'] = markdown_filter


def format_date(value):
    if isinstance(value, datetime):
        return value.strftime('%Y-%m-%d')
    return value


def set_target(attrs, new=False):
    p = urlparse(attrs[(None, 'href')])
    if p.netloc not in ['localhost']:
        attrs[(None, 'target')] = '_blank'
        attrs[(None, 'class')] = 'external'
    else:
        attrs.pop((None, 'target'), None)
    return attrs


def markdown_filter(text):
    html = markdown(text, extensions=['extra', 'fenced_code'])
    linker = Linker(callbacks=[set_target], skip_tags=['pre', 'code'])
    html = linker.linkify(html)
    return Markup(html)
