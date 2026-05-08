def myxml(tagname: str, content="", **attributes: str) -> str:
    """Generate an XML/HTML tag string with optional content and attributes."""
    attr_str = ' '.join(f'{key}="{value}"' for key, value in attributes.items())
    if attr_str:
        return f'<{tagname} {attr_str}>{content}</{tagname}>'
    else:
        return f'<{tagname}>{content}</{tagname}>'

# Example usage:
print(myxml('foo'))  # Output: <foo></foo>
print(myxml('foo', 'bar'))  # Output: <foo>bar</foo>
print(myxml('foo', 'bar', a='1', b='2', c='3'))  # Output: <foo a="1" b="2" c="3">bar</foo>

def myxml_c(tagname: str, content: str = "", **attributes) -> str:
    """Generate an XML/HTML tag string with optional content and attributes."""
    attrs = "".join(f' {k}="{v}"' for k, v in attributes.items())
    return f"<{tagname}{attrs}>{content}</{tagname}>"

print(myxml_c('foo'))  # Output: <foo></foo>
print(myxml_c('foo', 'bar'))  # Output: <foo>bar</foo>
print(myxml_c('foo', 'hello', a=1, b=2, c=3))

def myxml_l(tagname, content='', **kwargs):
    '''Generate an XML/HTML tag string with optional content and attributes.
    OJO: Prefixing a space to each attribute (f' {key}=...') elegantly avoids
    the if attr_str branch entirely.'''

    attrs = ''.join([f' {key}="{value}"'
                     for key, value in kwargs.items()])
    return f'<{tagname}{attrs}>{content}</{tagname}>'

print(myxml_l('foo'))  # Output: <foo></foo>
print(myxml_l('foo', 'bar'))  # Output: <foo>bar</foo>
print(myxml_l('foo', 'hello', a=1, b=2, c=3))