from django.shortcuts import render, get_object_or_404
from .models import Aluno
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def alunoView(request):
    alunos_list = Aluno.objects.all()
    return render(request, 'main/alunos.html', {'alunos_list': alunos_list})

def alunoIDview(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    return render(request, 'main/aluno.html', {'aluno': aluno})

def newAluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)

        