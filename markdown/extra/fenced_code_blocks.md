Markdown Extra introduced a syntax code block without indentation. Fenced code blocks are like Markdown’s regular code blocks, except that they’re not indented and instead rely on start and end fence lines to delimit the code block. The code block starts with a line containing three or more tilde ~ characters, and ends with the first line with the same number of tilde ~. For instance:

This is a paragraph introducing:

~~~
a one-line code block
~~~

You can also use backticks ` characters intead of tilde:

```
another code block
```

Indented code blocks cannot be used immediately following a list because the list indent takes precedence; fenced code block have no such limitation:

1.  List item

    Not an indented code block, but a second paragraph
    in the list item

~~~~
This is a code block, fenced-style
~~~~
