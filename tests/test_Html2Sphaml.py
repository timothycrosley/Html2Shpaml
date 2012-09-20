"""
    Tests converting html to more succinct shpaml markup
"""

from html2Shpaml import ShpamlTree as parse

EXAMPLE_1 = """
<p class="greeting">Hello World!</p>

<div class="content">
    <p id="message1">
        Goodbye Angle Brackets!
    </p>
    <p id="message2">
        Goodbye Close Tags!
    </p>
</div>
"""

EXAMPLE_1_DESIRED_OUTPUT = """
p.greeting | Hello World!
div.content
  p#message1 | Goodbye Angle Brackets!
  p#message2 | Goodbye Close Tags!"""

EXAMPLE_2 = """
<div class="section">
    <h5>Table Example</h5>
    <div class="prices">
        <table border="1">
          <tr>
            <th>Item</th>
            <th>Cost</th>
          </tr>
          <tr>
            <td>Orange</td>
            <td>0.75</td>
          </tr>
          <tr>
            <td>New car</td>
            <td>20,000</td>
          </tr>
          <tr>
            <td>DRY Markup</td>
            <td style="color: green">priceless</td>
          </tr>
        </table>
    </div>

    <h5>List Example</h5>
    <div class="list_example">
        <ol>
            <li>One</li>
            <li>Two</li>
            <li>
                <div class="longer_ordinal_description">
                    This is the
                    third item
                </div>
            </li>
        </ol>
    </div>
</div>
"""

EXAMPLE_2_DESIRED_OUTPUT = """
div.section
  h5 | Table Example
  div.prices
    table border=1
      tr
        th | Item
        th | Cost
      tr
        td | Orange
        td | 0.75
      tr
        td | New car
        td | 20,000
      tr
        td | DRY Markup
        td style=color:green; | priceless
  h5 | List Example
  div.list_example
    ol
      li | One
      li | Two
      li
        div.longer_ordinal_description
          This is the
          third item
"""

EXAMPLE_3 = """
For singleton tags like input and br, you might find it
most simple to just use raw HTML.
<br />
<br />

<div class="main">
    <form method="POST">
        <label for="id_description">Comment:</label>
        <br />
        <input type="text" value="example only" />
        <input type="submit" />
    </form>
</div>

<div class="alternative">
    <p>
        But you can also use this shortcut.
        <hr />
    </p>
</div>
"""

EXAMPLE_3_DESIRED_OUTPUT = """
For singleton tags like input and br, you might find it
most simple to just use raw HTML.
> br
> br
div.main
  form method=POST
    label for=id_description | Comment:
    > br
    > input type=text value="example only"
    > input type=submit
div.alternative
  p
    But you can also use this shortcut.
    > hr
"""

EXAMPLE_4 = """
see also:
    <a href="http://haml-lang.com/">HAML</a>
"""

EXAMPLE_4_DESIRED_OUTPUT = """
see also:
a href=http://haml-lang.com/ | HAML
"""

EXAMPLE_5 = """
<books>
    <book title="Design Patterns">
        <authors>
            <author>Erich Gamma</author>
            <author>Richard Helm</author>
            <author>Ralph Johnson</author>
            <author>John M. Vlissides</author>
        </authors>
    </book>
    <book title="An Introduction to Python">
        <authors>
            <author>Guido van Rossum</author>
            <author>Fred L. Drake</author>
        </authors>
    </book>
    <book title="War and Peace">
        <authors>
            <author>Leo Tolstoy</author>
        </authors>
    </book>
</books>
"""

EXAMPLE_5_DESIRED_OUTPUT = """
books
  book title="Design Patterns"
    authors
      author | Erich Gamma
      author | Richard Helm
      author | Ralph Johnson
      author | John M. Vlissides
  book title="An Introduction to Python"
    authors
      author | Guido van Rossum
      author | Fred L. Drake
  book title="War and Peace"
    authors
      author | Leo Tolstoy
"""

EMPTY_TAG_EXPECTED_OUTPUT = """
div
  ::comment
    empty
script
  ::comment
    empty
p
  ::comment
    empty
"""

def test_examples():
    """
        Tests rerunning the output examples from sphaml's against the reverse parser and assert the output is nice
        and tidy sphaml
    """
    assert str(parse(EXAMPLE_1)).strip() == EXAMPLE_1_DESIRED_OUTPUT.strip()
    assert str(parse(EXAMPLE_2)).strip() == EXAMPLE_2_DESIRED_OUTPUT.strip()
    assert str(parse(EXAMPLE_3)).strip() == EXAMPLE_3_DESIRED_OUTPUT.strip()
    assert str(parse(EXAMPLE_4)).strip() == EXAMPLE_4_DESIRED_OUTPUT.strip()
    assert str(parse(EXAMPLE_5)).strip() == EXAMPLE_5_DESIRED_OUTPUT.strip()

def test_emptyTag():
    """
        Ensure reverse parser works around issue with sphaml and empty tags
    """
    assert str(parse("""<div></div><script></script><p></p>""")).strip() == EMPTY_TAG_EXPECTED_OUTPUT.strip()




