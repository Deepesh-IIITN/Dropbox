from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import File
from .serializers import FileSerializer
from rest_framework.parsers import MultiPartParser
from utils.file_utils import FileUtils


class FileUploadAPIView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        try:
            file_data = request.FILES.get('file')
            file_meta_data = FileUtils.getFileMetaData(file_data)
            
            # Save file to local directory
            FileUtils.save_file(file_data, file_meta_data['file_name'])
            
            #save file meta data into DB
            serializer = FileSerializer(data=file_meta_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise ex
            return Response("Something went wrong", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FileReadAPIView(APIView):
    def get(self, request, file_id):
        try:
            file = File.objects.get(id=file_id)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FileSerializer(file)
        file_data = serializer.data
        file_data['file_path' ] = FileUtils.getAbsoluteFilePath(file_data['file_name'])
        
        return Response(serializer.data)

class FileUpdateAPIView(APIView):
    parser_classes = [MultiPartParser]

    def put(self, request, file_id):
        try:
            file = File.objects.get(id=file_id)
        except File.DoesNotExist:
            return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)

        # Update file if new file data is provided
        new_file_data = request.FILES.get('file')
        if new_file_data:
            file_data = request.FILES.get('file')
            
            file_meta_data = FileUtils.getFileMetaData(file_data)
            
            # Save file to local directory
            FileUtils.save_file(file_data, file_meta_data['file_name'])
            
            #save file meta data into DB
            serializer = FileSerializer(file, data=file_meta_data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileDeleteAPIView(APIView):
    def delete(self, request, file_id):
        try:
            file = File.objects.get(id=file_id)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FileListAPIView(APIView):
    def get(self, request):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        file_data = serializer.data
        
        #add file_path into response
        for index in range(len(file_data)):
            file_data[index]['file_path'] = FileUtils.getAbsoluteFilePath(file_data[index]['file_name'])

        return Response(file_data)
