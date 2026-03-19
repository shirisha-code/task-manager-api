from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer


class TaskListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    # GET → list tasks
    def get(self, request):
        if request.user.role == 'admin':
            tasks = Task.objects.all()
        else:
            tasks = Task.objects.filter(user=request.user)

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    # POST → create task
    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    # Helper method
    def get_task(self, request, pk):
        if request.user.role == 'admin':
            return Task.objects.get(id=pk)
        return Task.objects.get(id=pk, user=request.user)

    # GET single task
    def get(self, request, pk):
        task = self.get_task(request, pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    # UPDATE task
    def put(self, request, pk):
        task = self.get_task(request, pk)
        serializer = TaskSerializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # DELETE task
    def delete(self, request, pk):
        task = self.get_task(request, pk)
        task.delete()
        return Response({"message": "Deleted successfully"})