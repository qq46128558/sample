`inline links`

To create an inline link, use a set of regular parentheses immediately after the link text’s closing square bracket. Inside the parentheses, put the URL where you want the link to point, along with an optional title for the link, surrounded in quotes. For example:

This is [an example](http://example.com/ "Title") inline link.

[This link](http://example.net/) has no title attribute.

If you’re referring to a local resource on the same server, you can use relative paths:

See my [About](/about/) page for details.  

`reference links`

Reference-style links use a second set of square brackets, inside which you place a label of your choosing to identify the link:

This is [an example][id] reference-style link.

You can optionally use a space to separate the sets of brackets

This is [an example] [id] reference-style link.


Then, anywhere in the document, you define your link label like this, on a line by itself:

[id]: http://example.com/ "Optional Title Here"
---

The following three link definitions are equivalent:

    [foo]: http://example.com/  "Optional Title Here"
    [foo]: http://example.com/  'Optional Title Here'
    [foo]: http://example.com/  (Optional Title Here)
    [id]: <http://example.com/>  "Optional Title Here"
    [id]: http://example.com/longish/path/to/resource/here
    "Optional Title Here"

Link definition names may consist of letters, numbers, spaces, and punctuation — but they are not case sensitive. E.g. these two links:

[link text][a]
[link text][A]

are equivalent.

[a]: http://example.com "not case sensitive"
---

The implicit link name shortcut allows you to omit the name of the link, in which case the link text itself is used as the name. Just use an empty set of square brackets — e.g., to link the word “Google” to the google.com web site, you could simply write:

[Google][]

And then define the link:

[Google]: http://google.com/
---

Because link names may contain spaces, this shortcut even works for multiple words in the link text:

Visit [Daring Fireball][] for more information.

And then define the link:

[Daring Fireball]: http://daringfireball.net/
---


Link definitions can be placed anywhere in your Markdown document. I tend to put them immediately after each paragraph in which they’re used, but if you want, you can put them all at the end of your document, sort of like footnotes.

I get 10 times more traffic from [Google] [1] than from
[Yahoo] [2] or [MSN] [3].

  [1]: http://google.com/        "Google"
  [2]: http://search.yahoo.com/  "Yahoo Search"
  [3]: http://search.msn.com/    "MSN Search"


For comparison, here is the same paragraph written using Markdown’s inline link style:

I get 10 times more traffic from [Google](http://google.com/ "Google")
than from [Yahoo](http://search.yahoo.com/ "Yahoo Search") or
[MSN](http://search.msn.com/ "MSN Search").

---

