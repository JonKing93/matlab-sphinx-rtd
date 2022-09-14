"""
    pygments.styles.matlab
    ~~~~~~~~~~~~~~~~~~~~~~

    Style inspired by the MATLAB editor. Note this is not meant to be a complete style. Instead, it's meant to mimic the default syntax highlighting of the MATLAB editor.

    :copyright: Copyright 2022 by Jonathan King
    :license: MIT
"""

from pygments.style import Style
from pygments.token import Token, Keyword, String, Comment, Generic


class MatlabStyle(Style):
    """
    Style inspired by the MATLAB editor. Note this is not meant to be a complete style. Instead, it's meant to mimic the default syntax highlighting of the MATLAB editor.
    """

    styles = {
        Token:           '#000000',       # Black text by default
        Keyword:         '#0000FF',       # Blue keywords
        String:          '#AA04F9',       # Pink strings
        Comment:         '#028009',       # Green comments
        Generic.Strong:  'bold #028009'   # Bold any %% comment sections
    }
