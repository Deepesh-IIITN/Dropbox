import os
from datetime import datetime

class FileUtils:
    @staticmethod
    def save_file(file_data, file_name):
        """
        Save the uploaded file to the specified directory.

        Args:
            file_data (UploadedFile): The file data to be saved.
            file_name (str): The name of the file.

        Returns:
            str: The path where the file is saved.
        """
        # Define the directory where files will be saved
        save_directory = 'assets/uploaded_files'

        # Create the directory if it doesn't exist
        os.makedirs(save_directory, exist_ok=True)

        # Construct the full file path
        file_path = os.path.join(save_directory, file_name)

        # Open the file and write the chunks of data
        with open(file_path, 'wb') as destination:
            for chunk in file_data.chunks():
                destination.write(chunk)

        return file_path
    
    @staticmethod
    def getAbsoluteFilePath(file_name):
        # Define the directory where files will be saved
        save_directory = 'assets/uploaded_files'

        # Create the directory if it doesn't exist
        os.makedirs(save_directory, exist_ok=True)

        # Construct the full file path
        file_path = os.path.join(save_directory, file_name)
        return os.path.abspath(file_path)
    
    @staticmethod
    def getFileMetaData(file_data):

        #cuurent date time
        current_datetime = datetime.now()
        # Convert datetime to a number representation
        datetime_number = str(int(current_datetime.timestamp()))
        file_extention = file_data.name.split(".")

        print(datetime_number, file_extention)

        if len(file_extention) > 1:
             file_extention = file_extention[1]
        else:
            file_extention = ""

        return {
            "file_name": datetime_number+"."+file_extention,
            "size": file_data.size,
            "file_type": file_data.content_type
        }
        