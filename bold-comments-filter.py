class BoldCommentsFilter(Filter):

    def __init__(self, **options):
        Filter.__init__(self, **options)
        self.class_too = get_bool_opt(options, 'classtoo')

    def filter(self, lexer, stream):
        for ttype, value in stream:

            # If a token is a comment that begins with %% and a space,
            # convert it to a Generic.Strong token
            if ttype is Comment and len(value)>1 and value[1]=='%' and (len(value)==2 or len[2]==' ')
                ttype = Generic.Strong
            yield ttype, value
