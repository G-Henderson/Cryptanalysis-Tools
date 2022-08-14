
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
        temp = ""

        # Iterate through message
        for i in range(len(message)):
            # Get the current character
            current_char = message[i]
            # Check if current char is in alphabet or is a space.
            if (current_char.lower() in self.ALPHABET) or (current_char == " "):
                temp += current_char

        # Transfer the result stored in the temp variable into the message variable
        result = temp

        # Return the message
        return result


    def remove_spaces(self, message: str) -> str:
        """
        Removes all the spaces from the message (leaves punctuation)
        """

        # Remove the spaces from the text
        result = message.replace(" ", "")

        # Return the text
        return result

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