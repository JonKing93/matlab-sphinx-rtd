class BoldCommentFilter(Filter):
    """Converts comments beginning with %% to Generic.Strong tokens to support bold styling"""

    def __init__(self, **options):
        Filter.__init__(self, **options)

    def filter(self, lexer, stream):
        for ttype, value in stream:

            # If a token is a comment that begins with %% and a space,
            # convert it to a Generic.Strong token
            if ttype is Comment:
                length = len(value)
                if length>1 and value[1]=='%' and (length==2 or value[2]==' '):
                    ttype = Generic.Strong
            yield ttype, value
