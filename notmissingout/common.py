from sanitizer.models import SanitizedTextField


class HtmlField(SanitizedTextField):
    def __init__(self, **kwargs):
        kwargs_with_defaults = dict(
            allowed_tags=[
                'p',
                'br',
                'blockquote',
                'pre',
                'h1',
                'h2',
                'h3',
                'h4',
                'h5',
                'h6',
                'b',
                'i',
                'u',
                'strike',
                'sup',
                'sub',
                'div',
                'span',
                'font',
                'ul',
                'ol',
                'li',
                'a',
                'img',
                'hr',
                'table',
                'tbody',
                'tr',
                'td',
                'th',
            ],
            allowed_attributes=[
                'style',
                'href',
                'src',
                'color',
            ],
            allowed_styles=[
                'background-color',
                'line-height',
                'font-size',
                'text-align',
                'margin-left',
            ],
            strip=True,
            help_text="Body of the recipe, in HTML format.",
        )
        kwargs_with_defaults.update(kwargs)
        super(HtmlField, self).__init__(**kwargs_with_defaults)
