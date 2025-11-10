# calculator/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import View
from django.http import FileResponse
from django.conf import settings
import os

class CalculatorView(APIView):
    def post(self, request):
        num1 = request.data.get("num1")
        num2 = request.data.get("num2")
        operation = request.data.get("operation")

        try:
            num1 = float(num1)
            num2 = float(num2)
        except (TypeError, ValueError):
            return Response({"error": "Invalid numbers"}, status=status.HTTP_400_BAD_REQUEST)

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return Response({"error": "Division by zero"}, status=status.HTTP_400_BAD_REQUEST)
            result = num1 / num2
        else:
            return Response({"error": "Invalid operation"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"result": result})

class FrontendAppView(View):
    def get(self, request):
        index_file_path = os.path.join(settings.REACT_APP_DIR, 'index.html')
        try:
            return FileResponse(open(index_file_path, 'rb'))
        except FileNotFoundError:
            return FileResponse(b"Build your React app first.", status=404)
