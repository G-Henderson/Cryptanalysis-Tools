
class TextUtils:

    """
    Class for general text manipulation
    """

    def __init__(self, my_message) -> None:
        # Setup text variables
        self.original_text = my_message
        self.message = self.getOriginal_text()

        # Create a alphabet variables
        self.ALPHABET = "abcdefghijklmnopqrstuvwxyz"


    def remove_punctuation(self) -> str:
        """
        Removes all the spaces from the message (leaves spaces)
        """

        # Create temporary variable to hold text
        temp = ""

        # Iterate through message
        for i in range(len(self.text)):
            # Get the current character
            current_char = self.text[i]
            # Check if current char is in alphabet or is a space.
            if (current_char.lower() in self.ALPHABET) or (current_char == " "):
                temp += current_char

        # Transfer the result stored in the temp variable into the message variable
        self.message = temp

        # Return the message
        return self.message


    def remove_spaces(self) -> str:
        """
        Removes all the spaces from the message (leaves punctuation)
        """

        # Remove the spaces from the text
        self.message = self.message.replace(" ", "")

        # Return the text
        return self.message

    def getOriginal_text(self) -> str:
        # Return the value original text before manipulation
        return self.original_text