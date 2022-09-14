# matlab-sphinx-rtd
A collection of hacks for documenting Matlab code using Sphinx and the ReadTheDocs theme.

This repository contains various files and code snippets I use to improve the look of Matlab code documented using Sphinx with the ReadTheDocs theme. The contents of the repository are:

1. A custom Pygments style and filter that mimic the default code highlighting in the Matlab editor
2. CSS classes that mimic the look of input-output code blocks in official Matlab documentation
3. CSS classes the mimic the look and layout of documentation pages for official Matlab functions

The repository contains the following contents:

* matlab-color-codes.txt
    A list of default color codes used by the Matlab editor to implement code highlighting.
* matlab.py
    A custom Pygments style that mimics the Matlab editor
* bold-comments-filter.py
    A custom Pygments filter that assigns the Generic.Strong token to %% comments
* highlighting.py
    A hacked file in the sphinx package that implements the bold-comments filter
* matlab-io.css
    CSS classes that implement input-output code blocks
* accordion.css
    A CSS class that implements collapsible accordion sections
* matlab-docs.css
    CSS classes that mimic the layout and style of official Matlab function documentation pages

More detailed descriptions, and instructions for implementing the hacks, are given below. I created these hacks using Pygments 2.13, Sphinx 5.1.1, and sphinx-rtd-theme 1.0.0, although I anticipate these hacks will work in later versions.

### `matlab-color-codes.txt`

This file lists the default color codes used by the Matlab editor to implement code highlighting. This file isn't actually used in any hacks, but it can be useful when developing new features.


### `matlab.py`

This contains a custom Pygments theme to highlight code in a style mimicking the Matlab editor. Along with basic Pygments code tokens, the file implements a style for Generic.Strong. This allows %% comments to be given a custom style when combined with the bold-comments filter in the next section.

To use this hack:
1. Navigate to `path/to/./Python/Lib/site-packages/pygments/styles/`
2. Add this file to the folder
3. Edit `__init__.py` to include the line
```
    'matlab': 'matlab::MatlabStyle'
````
in the `STYLE_MAP` variable near the top of the file.


### `bold-comments-filter.py`

This file creates a custom Pygments filter. The filter locates comments that begin with `%% ` and converts them from a Comment token to a Generic.Strong token. This allows `%%` comments to be bolded in the highlighted code. This file is a code snippet that needs to be added to an existing file in the Pygments package. Specifically:

1. Navigate to `path/to/./Python/Lib/site-packages/pygments/filters/`
2. Edit `__init__.py` to include the code snippet in `bold-comments-filter.py`
3. Add the line:
```
    'boldcomment':    BoldCommentFilter,
```
to the `FILTERS` variable at the end of the file.


### `highlighting.py`

This file is a hacked version of the `highlighting.py` module from the sphinx package. Sphinx does not allow you to implement Pygments filters when calling code, so we need to modify its code highlighting routine to include our bold-comment filter. Note that this file is just an example - you shouldn't copy it directly into your sphinx package, because newer versions of sphinx may have altered this file. Instead, edit the `highlighting.py` file in your sphinx package to mimic this example:

1. Navigate to `path/to/./Python/Lib/site-packages/sphinx/` and open ``highlighting.py` for editing

2. Near the top of the file, edit the line:
```
from pygments.lexers import (CLexer, Python3Lexer, PythonConsoleLexer, PythonLexer, RstLexer,
                             TextLexer, get_lexer_by_name, guess_lexer)
```
to also import the MatlabLexer
```
from pygments.lexers import (MatlabLexer, CLexer, Python3Lexer, PythonConsoleLexer, PythonLexer, RstLexer,
                             TextLexer, get_lexer_by_name, guess_lexer)
```

3. In the ``get_lexer`` function, immediately before the ``return lexer`` statement (near line 166), add the following code snippet:
```
        if type(lexer) == MatlabLexer:
            lexer.add_filter('boldcomment')
````


### Using custom CSS styles

To use any of the following CSS styles in sphinx

1. Navigate to `source/static/css/` folder of your sphinx project
2. Add the file to the folder.
3. Edit the sphinx configuration file `conf.py` to include the lines:
```
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ["css/output.css"]
```

Note that these theme modifications were developed for the ReadTheDocs theme, so we included that theme explicitly in the above code. You can still use a different theme if you prefer, but it might not look as good.


### `matlab-io.css`

This css file describes classes for input-output (IO) code blocks that mimic the style of IO blocks in official Matlab documentation. This style removes the margin between inputs and outputs.These code blocks are set so there is no margin between the input and output. Output blocks match the background color of the page and receive no code highlighting. Standard output messages are colored black, error messages are red, and warning messages are orange.

To implement an IO block in a reST file, use the ``.. code::`` directive, and use the ``:class:`` option to indicate the type of code block. The type may either be ``input``, ``output``, ``output m-error`` or ``output m-warning``. (The `m-` prefix is because the rtd theme already defines `error` and `warning` classes.). So for example:
```
.. code::
    :class: input

    Here is some input code

.. code::
    :class: output

    Here is the output
```
would create a standard IO block. Similarly:
```
```
.. code::
    :class: input

    Here is some input code

.. code::
    :class: output m-error

    Here is an error message
```
would create an IO block for an error message output.



### `accordion.css`

This css file describes a class that implements a collapsible accordion section. It can be used for things like examples and Input/Output parameters.

TODO: Add more detail to this section. For now, you can navigate to the DASH repository, and run the `documentDASH` function in the `doc_source` directory. Then look at the generated rst files for details on how to implement the accordions.


### `matlab-docs.css`

This css file describes some classes that help mimic the style and layout of official Matlab function documentation pages.

TODO: Add more details to this section. These classes are based on the reST parsers in the DASH toolbox.
