class TextUtils:

    """
    Class for general text manipulation
    """

    def __init__(self) -> None:
        # Create a alphabet variables
        self.ALPHABET = "abcdefghijklmnopqrstuvwxyz"


    def remove_punctuation(self, message: str) -> str:
        """
        Removes all the spaces from the message (leaves spaces)
        """

        # Create temporary variable to hold text
        result = ""

        # Iterate through message
        for char in message:
            # Check if current char is in alphabet or is a space.
            if (char.lower() in self.ALPHABET) or (char == " "):
                result += char

        # Return the message
        return result


    def remove_spaces(self, message: str) -> str:
        """
        Removes all the spaces from the message (leaves punctuation)
        """

        # Remove the spaces from the text and return the result
        return message.replace(" ", "")
    

    def only_letters(self, message: str) -> str:
        """
        Removes all characters that aren't letters
        """

        # Remove the spaces from the text
        result = self.remove_spaces(message)

        # Remove punctuation
        result = self.remove_punctuation(result)

        # Return the text
        return result