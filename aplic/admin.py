from django.contrib import admin

from .models import Curso, Professor, Aluno, Disciplina, Turma, Avaliacao, Nota, Arquivo


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria')

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'titulacao')

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'curso')

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'carga_horaria')

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('ano', 'semestre', 'turma', 'disciplina')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'turma', 'data_publicacao', 'data_entrega', 'valor_avaliacao')

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('avaliacao', 'turma', 'aluno', 'valor')

@admin.register(Arquivo)
class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nome_do_arquivo')