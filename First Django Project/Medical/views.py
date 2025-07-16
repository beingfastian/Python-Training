# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib import messages
# from .models import Patient
# from .forms import PatientForm

# def patient_list(request):
#     patients = Patient.objects.all()
#     return render(request, 'patients/list.html', {'patients': patients})

# def patient_detail(request, id):
#     patient = get_object_or_404(Patient, id=id)
#     return render(request, 'patients/detail.html', {'patient': patient})

# def patient_create(request):
#     if request.method == 'POST':
#         form = PatientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Patient created successfully!')
#             return redirect('patient_list')
#     else:
#         form = PatientForm()
#     return render(request, 'patients/form.html', {'form': form, 'title': 'Add Patient'})

# def patient_edit(request, id):
#     patient = get_object_or_404(Patient, id=id)
#     if request.method == 'POST':
#         form = PatientForm(request.POST, instance=patient)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Patient updated successfully!')
#             return redirect('patient_detail', id=patient.id)
#     else:
#         form = PatientForm(instance=patient)
#     return render(request, 'patients/form.html', {'form': form, 'title': 'Edit Patient'})

# def patient_delete(request, id):
#     patient = get_object_or_404(Patient, id=id)
#     if request.method == 'POST':
#         patient.delete()
#         messages.success(request, 'Patient deleted successfully!')
#         return redirect('patient_list')
#     return render(request, 'patients/delete.html', {'patient': patient})


from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import PatientSerializer
from .models import Patient
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
class PatientViewSet(viewsets.ModelViewSet):
    
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
    @action(detail=False, methods=['get','post', 'put', 'delete', 'patch', 'update'])
    def search(self, request):
        name = request.query_params.get('name', None)
        if name:
            patients = Patient.objects.filter(name__icontains=name)
            serializer = self.get_serializer(patients, many=True)
            return Response(serializer.data)
        return Response({'error': 'Name parameter is required'}, 
                       status=status.HTTP_400_BAD_REQUEST)