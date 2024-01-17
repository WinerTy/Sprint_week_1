import django_filters
from rest_framework.response import Response
from database.models import Users, Coords, Level, Images, Perevals
from rest_framework import viewsets, status
from .serializers import UsersSerializer, CoordsSerializer, LevelSerializer, ImagesSerializer, PerevalsSerializer


class UsersViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['fam', 'name', 'otc', 'email']


class CoordsViewset(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewset(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImagesViewset(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PerevalsViewset(viewsets.ModelViewSet):
    queryset = Perevals.objects.all()
    serializer_class = PerevalsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['beauty_title', 'title', 'add_time', 'user__email']

    def create(self, request,  *args, **kwargs):
        if self.action == 'create':
            serializer = PerevalsSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': 'Данные успешно отправленны и внесены в Базу Данных!',
                        'id': serializer.instance.pk,
                    }
                )

            if status.HTTP_400_BAD_REQUEST:
                print(serializer.errors)
                return Response(
                    {
                        'status': status.HTTP_400_BAD_REQUEST,
                        'message': 'неправильная валидация запроса',
                        'id': None,
                    }
                )

            if status.HTTP_500_INTERNAL_SERVER_ERROR:
                return Response(
                    {
                        'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': 'Ошибка при выполнении операции',
                        'id': None,
                    }
                )
        return super().create(request, *args, **kwargs)