##### Sending and receiving responses in DRF.

n Django REST Framework (DRF):

To send responses, use Response from rest_framework.response.

from rest_framework.response import Response

return Response({"message": "Success"}, status=200)


To receive requests, use request.data for POST/PUT/PATCH and request.query_params for GET.

@api_view(['POST'])
def create_student(request):
    data = request.data  # incoming JSON
    return Response(data, status=201)