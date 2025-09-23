from rest_framework.generics import ListAPIView
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Project


class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
