from elem import *

class Html(Elem):
    def __init__(self, content=None):
        super().__init__(tag="html", content=content)

class Head(Elem):
    def __init__(self, content=None):
        super().__init__(tag="head", content=content)

class Body(Elem):
    def __init__(self, content=None):
        super().__init__(tag="body", content=content)

class Title(Elem):
    def __init__(self, content=None):
        super().__init__(tag="title", content=content)

class Meta(Elem):
    def __init__(self, attr={}):
        super().__init__(tag="meta", attr=attr, tag_type="simple")

class Img(Elem):
    def __init__(self, attr={}):
        super().__init__(tag="img", attr=attr, tag_type="simple")

class Table(Elem):
    def __init__(self, content=None):
        super().__init__(tag="table", content=content)

class Th(Elem):
    def __init__(self, content=None):
        super().__init__(tag="th", content=content)

class Tr(Elem):
    def __init__(self, content=None):
        super().__init__(tag="tr", content=content)

class Td(Elem):
    def __init__(self, content=None):
        super().__init__(tag="td", content=content)

class Ul(Elem):
    def __init__(self, content=None):
        super().__init__(tag="ul", content=content)

class Ol(Elem):
    def __init__(self, content=None):
        super().__init__(tag="ol", content=content)

class Li(Elem):
    def __init__(self, content=None):
        super().__init__(tag="li", content=content)

class H1(Elem):
    def __init__(self, content=None):
        super().__init__(tag="h1", content=content)

class H2(Elem):
    def __init__(self, content=None):
        super().__init__(tag="h2", content=content)

class P(Elem):
    def __init__(self, content=None): 
        super().__init__(tag="p", content=content)

class Div(Elem):
    def __inti__(self, content=None):
        super().__init__(content=content)

class Span(Elem):
    def __init__(self, attr={}):
        super().__init__(tag="span", attr=attr)

class Hr(Elem):
    def __init__(self, attr={}):
        super().__init__(tag="hr", attr=attr)

class Br(Elem):
    def __init__(self, attr={}):
        super().__init__(tag="br", attr=attr)

def main():
    head = Head(Title(Text('/"Hello ground!/"')))
    body = Body(H1([Text('/"Oh no, not again!/"'), Img({"src" : "http://i.imgur.com/pfp3T.jpg"})]))
    print(Html([head, body]))

if __name__ == '__main__':
    main()
