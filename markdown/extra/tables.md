Markdown Extra has its own syntax for simple tables. A “simple” table looks like this:

First Header  | Second Header
-|-
Content Cell  | Content Cell
Content Cell  | Content Cell


You can specify alignment for each column by adding colons to separator lines. A colon at the left of the separator line will make the column left-aligned; a colon on the right of the line will make the column right-aligned; colons at both side means the column is center-aligned.

| Item      | Value |
| -| -:|
| Computer  | $1600 |
| Phone     |   $12 |
| Pipe      |    $1 |

You can apply span-level formatting to the content of each cell using regular Markdown syntax:

| Function name | Description                    |
| ------------- | ------------------------------ |
| `help()`      | Display the help window.       |
| `destroy()`   | **Destroy your computer!**     |