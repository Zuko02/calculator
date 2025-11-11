# calculator/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CalculatorSerializer

class CalculatorView(APIView):
    def post(self, request):
        serializer = CalculatorSerializer(data=request.data)
        if serializer.is_valid():
            num1 = serializer.validated_data['num1']
            num2 = serializer.validated_data['num2']
            operation = serializer.validated_data['operation']

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

            return Response({"result": result}, status=status.HTTP_200_OK)
        
        # If validation fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
