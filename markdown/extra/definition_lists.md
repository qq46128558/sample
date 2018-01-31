
Markdown Extra implements definition lists. Definition lists are made of terms and definitions of these terms, much like in a dictionary.

Apple
:   Pomaceous fruit of plants of the genus Malus in the family Rosaceae.

Orange
:   The fruit of an evergreen tree of the genus Citrus.


Each of the preceding definition lists will give the same HTML result:
~~~
<dl>
<dt>Apple</dt>
<dd>Pomaceous fruit of plants of the genus Malus in 
the family Rosaceae.</dd>

<dt>Orange</dt>
<dd>The fruit of an evergreen tree of the genus Citrus.</dd>
</dl>
~~~

Definition lists can have more than one definition associated with one term:

Apple
:   Pomaceous fruit of plants of the genus Malus in the family Rosaceae.
:   An American computer company.

Orange
:   The fruit of an evergreen tree of the genus Citrus.

You can also associate more than one term to a definition:

Term 1
Term 2
:   Definition a

Term 3
:   Definition b


---
And just like regular list items, definitions can contain multiple paragraphs, and include other block-level elements such as blockquotes, code blocks, lists, and even other definition lists.


Term 1

:   This is a definition with two paragraphs. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

:   Second definition for term 1, also wrapped in a paragraph because of the blank line preceding it.

Term 2

:   This definition has a code block, a blockquote and a list.

        code block.

    > block quote
    > on two lines.

    1.  first list item
    2.  second list item