Footnotes work mostly like reference-style links. A footnote is made of two things: a marker in the text that will become a superscript number; a footnote definition that will be placed in a list of footnotes at the end of the document. A footnote looks like this:

That's some text with a footnote.[^1]

[^1]: And that's the footnote.

Footnotes can contain block-level elements, which means that you can put multiple paragraphs, lists, blockquotes and so on in a footnote. It works the same as for list items: just indent the following paragraphs by four spaces in the footnote definition:


That's some text with a footnote.[^2]

[^2]: And that's the footnote.

    That's the second paragraph.

If you want things to align better, you can leave the first line of the footnote empty and put your first paragraph just below:

That's some text with a footnote.[^XX]

[^XX]:
    And that's the footnote.

    That's the second paragraph.

