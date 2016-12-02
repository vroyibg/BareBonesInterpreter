ENDMARK = "\0"


# -----------------------------------------------------------------------
#
#               Character
#
# -----------------------------------------------------------------------
class Character:
    """
    A Character object holds
        - one character (self.cargo)
        - the index of the character's position in the sourceText.
        - the index of the line where the character was found in the sourceText.
        - the index of the column in the line where the character was found in the sourceText.
        - (a reference to) the entire sourceText (self.sourceText)

    This information will be available to a token that uses this character.
    If an error occurs, the token can use this information to report the
    line/column number where the error occurred, and to show an image of the
    line in sourceText where the error occurred.
    """

    # -------------------------------------------------------------------
    #               Constructor
    # -------------------------------------------------------------------
    def __init__(self, char, line_index, column_index, source_index, source_text):
        self.char = char
        self.sourceIndex = source_index
        self.line_index = line_index
        self.column_index = column_index
        self.source_text = source_text

    # -------------------------------------------------------------------
    # return a displayable string representation of the Character object
    # -------------------------------------------------------------------
    def __str__(self):
        cargo = self.char
        if cargo == " ":
            cargo = "   space"
        elif cargo == "\n":
            cargo = "   newline"
        elif cargo == "\t":
            cargo = "   tab"
        elif cargo == ENDMARK:
            cargo = "   eof"

        return (
            str(self.line_index).rjust(6)
            + str(self.column_index).rjust(4)
            + "  "
            + cargo
        )
