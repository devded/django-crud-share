from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import ParseError
# Create your views here.
import fitparse
import json

import pathlib

from fitfileviewer.utils import get_file_id_data, get_record_data, get_event_data, get_session_data, get_activity_data


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
                fitfile = fitparse.FitFile(f)

                file_id_raw = get_file_id_data(fitfile)
                file_id_data = json.loads(file_id_raw)
                record_raw = get_record_data(fitfile)
                record_data = json.loads(record_raw)
                event_raw = get_event_data(fitfile)
                event_data = json.loads(event_raw)
                session_raw = get_session_data(fitfile)
                session_data = json.loads(session_raw)
                activity_raw = get_activity_data(fitfile)
                activity_data = json.loads(activity_raw)

                data = {
                    "status": "ok",
                    "file_id": file_id_data,
                    "record": record_data,
                    "event": event_data,
                    "session": session_data,
                    "activity": activity_data,
                }
                return Response(data)
            else:
                return Response({"status": "error", "message": "File extension is not .fit"})

        if 'file' not in request.data:
            raise ParseError("Empty content")
            return Response({"status": "Failed"})

        
