from rest_framework.generics import ListAPIView
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Project


class ProjectListView(ListAPIView):
    queryset = Project.objects.all().order_by("-updated_at")
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
