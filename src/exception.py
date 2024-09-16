import sys

# Function to capture and return detailed error information
def error_message_detail(error, error_detail: sys):
    # Extracts the exception details from the error stack trace
    _, _, exc_tb = error_detail.exc_info()

    # Retrieves the file name where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Formats a detailed error message with file name, line number, and error message
    error_message = "Error occurred in python script name {0} on line number [{1}] with error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    # Returns the formatted error message
    return error_message

# Custom exception class to handle and log errors with more details
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Initialize the base Exception class with the error message
        super().__init__(error_message)

        # Call the error_message_detail function to get the detailed error message
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    # Optionally, you can define a __str__ method to customize how the exception is printed
    def __str__(self):
        return self.error_message
