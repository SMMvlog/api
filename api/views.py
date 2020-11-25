from django.shortcuts import render
from .models import Skill,Experience,Education
from .serializers import SkillSerializer,ExperienceSerializer,EducationSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView

# Skill
class SkillListCreate(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    

class SkillRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

# Education
class EduListCreate(ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class EduRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

# Experience
class ExpListCreate(ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class ExpRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer