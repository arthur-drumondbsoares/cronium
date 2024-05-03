from rest_framework.response import Response
from rest_framework import status


class HttpMixin():
        def perform_get(self, obj_class, obj_id, serializer_class, request):
            try:
                obj = obj_class.objects.get(pk=obj_id)
                serializer = serializer_class(obj)
                return Response(serializer.data)
            except:
                return Response({"error": "Object not found"}, status=404)
            

        def perform_post(self, obj_class, serializer_class, request, foreign_key_class = [None]):
             #When creating any instance other than user 
            try:
                if foreign_key_class:
                    if len(foreign_key_class) ==2:
                        fields = {}
                        for key, value in request.query_params.items():
                            fields.update({key: value})
                        fields[foreign_key_class[0].__name__.lower() + "_id"]=  int(fields[foreign_key_class[0].__name__.lower() + "_id"])
                        fields[foreign_key_class[1].__name__.lower() + "_id"] = int(fields[foreign_key_class[1].__name__.lower() + "_id"])
                        obj = obj_class.objects.create(**fields)
                        serializer = serializer_class(obj)
                        return Response(serializer.data)                      

                    else:
                        foreign_key_class = foreign_key_class[0]
                        fields = {}
                        for key, value in request.query_params.items():
                            fields.update({key: value})
                        fields[foreign_key_class.__name__.lower() + "_id"] = int(fields[foreign_key_class.__name__.lower() + "_id"])
                        obj = obj_class.objects.create(**fields)
                        serializer = serializer_class(obj)
                        return Response(serializer.data)
                else: #When creating an user
                    fields = dict(request.query_params)
                    obj = obj_class.objects.create(**fields)
                    serializer = serializer_class(obj)
                    return Response(serializer.data)
            except Exception as e:
                return Response({"error": str(e)}, status=400)
            





        def perform_delete(self, obj_class, obj_id, request):
            try:
                obj = obj_class.objects.get(pk=obj_id)
                obj.delete()
                return Response({'message': 'Object deleted sucefully'})
            except Exception as e:
                return Response({"error": str(e)}, status=400)





        def perform_put(self, obj_class, obj_id, serializer_class, request):
            try:
                obj = obj_class.objects.get(pk=obj_id)
                serializer_data = request.query_params.copy()
                serializer = serializer_class(obj, data=serializer_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": str(e)}, status=400)