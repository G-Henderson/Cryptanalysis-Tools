
class Test(object):

    def __init__(self, details) -> None:
        # Print the details
        print(details)

        # Create empty variables
        self.ex_output_data = None
        self.my_test = None
    

    def setTest(self, my_test, expected_output) -> None:
        """
        Takes the test
        """

        self.my_test = my_test
        self.ex_output_data = expected_output

    def test(self) -> bool:
        """
        Runs the test and returns whether or not it passed
        """
        
        # Run the test
        actual_output = self.my_test()

        # Check if the actual result is the same as expected
        if (actual_output == self.ex_output_data):
            # If it is return true
            return True
        
        else:
            # Else return false
            return False

    def print_output(self) -> None:
        """
        Runs the test and outputs the result
        """

        # Get the result by running the test
        result = self.test()

        if (result):
            print("Passed")
        else:
            print("Failed")