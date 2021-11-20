from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import ParseError
# Create your views here.
import fitparse
import json

import pathlib

from fitfileviewer.utils import get_file_id_data

class FitFileViewerServerCheckView(APIView):
    
    # def get(self, request, format=None):
    #     return Response({"status": "ok"})
    
    parser_class = (FileUploadParser, )
    def post(self, request, format = None):
        if 'file' in request.data:
            file_extension = pathlib.Path('my_file.txt').suffix
            print("File Extension: ", file_extension)
            if file_extension == '.fit' or '.txt':
                print("File Detect")
                f = request.data['file']
                content_type = f.content_type
                print(content_type)
                fitfile = fitparse.FitFile(f)
                result = get_file_id_data(fitfile)
                file_id = json.loads(result)
                data = {
                    "status": "ok",
                    "file_id": file_id,
                }
                return Response(data)
            else:
                return Response({"status": "error", "message": "File extension is not .fit"})

        if 'file' not in request.data:
            raise ParseError("Empty content")
            return Response({"status": "Failed"})

        
