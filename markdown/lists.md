Unordered lists use asterisks, pluses, and hyphens — interchangably — as list markers:

*   Red
*   Green
*   Blue
+   Red
+   Green
+   Blue
-   Red
-   Green
-   Blue

Ordered lists use numbers followed by periods:

1. Bird
2. McHale
3. Parish

It’s important to note that the actual numbers you use to mark the list have no effect on the HTML output Markdown produces.

1. Bird
1. McHale
1. Parish

To make lists look nice, you can wrap items with hanging indents:

*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.

But if you want to be lazy, you don’t have to:

*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
Suspendisse id sem consectetuer libero luctus adipiscing.

If list items are separated by blank lines, Markdown will wrap the items in \<p\> tags in the HTML output.

*   Bird

*   Magic

List items may consist of multiple paragraphs. Each subsequent paragraph in a list item must be indented by either 4 spaces or one tab:

1.  This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.

It looks nice if you indent every line of the subsequent paragraphs, but here again, Markdown will allow you to be lazy:

*   This is a list item with two paragraphs.

    This is the second paragraph in the list item. You're
only required to indent the first line. Lorem ipsum dolor
sit amet, consectetuer adipiscing elit.

*   Another item in the same list.

To put a blockquote within a list item, the blockquote’s > delimiters need to be indented:

*   A list item with a blockquote:

	> This is a blockquote
    > inside a list item.

To put a code block within a list item, the code block needs to be indented twice — 8 spaces or two tabs:

*   A list item with a code block:

        <code goes here>


It’s worth noting that it’s possible to trigger an ordered list by accident, by writing something like this:

1986. What a great season.
1987. 

In other words, a number-period-space sequence at the beginning of a line. To avoid this, you can backslash-escape the period:

1986\. What a great season.
