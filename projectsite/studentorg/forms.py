from django.forms import ModelForm
from django import forms
from .models import Organization, OrgMember, Student, College


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

class OrgmemberForm(ModelForm):
    class Meta:
        model = OrgMember
        fields = "__all__"
        
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class CollegeForm(ModelForm):
    class Meta:
        model = College 
        fields = "__all__"