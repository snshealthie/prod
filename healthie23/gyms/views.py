from gyms.models import Gym
from gyms.serializers import GymSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics
from rest_framework.views import APIView


class GymList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'gym_list.html'

    def get(self, request):
        queryset = Gym.objects.all()
        return Response({'profiles': queryset})



class GymDetail(generics.RetrieveAPIView):
    """
    A view that returns a templated HTML representation of a given user.
    """
    queryset = Gym.objects.all()
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'gym': self.object}, template_name='gym_detail.html')