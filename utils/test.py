class Test(object):

    def __init__(self, details) -> None:
        # Setup variables
        self.test_details = details
        self.expected_output_data = None
        self.my_test = None
    

    def setTest(self, my_test, expected_output) -> None:
        """
        Sets the test
        """

        self.my_test = my_test
        self.expected_output_data = expected_output

    def test(self) -> bool:
        """
        Runs the test and returns whether or not it passed
        """
        
        # Run the test
        actual_output = self.my_test()

        # Check if the actual result is the same as expected
        if (actual_output == self.expected_output_data):
            # If it is return true
            return True
        
        else:
            print(f"Actual output: {actual_output}")
            # Else return false
            return False

    def run(self) -> None:
        """
        Runs the test and outputs the result
        """

        # Print test details
        print(self.test_details)

        # Get the result by running the test
        result = self.test()

        if (result):
            print("PASSED")
        else:
            print("FAILED")