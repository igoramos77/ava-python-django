from django.contrib import admin

from .models import Curso, Professor, Aluno, Disciplina, Turma, Avaliacao, Nota, Arquivo


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria')
    search_fields = ('nome', 'carga_horaria')
    list_per_page = 15


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'titulacao')
    search_fields = ('nome', 'titulacao')
    list_filter = ('titulacao',)
    list_per_page = 15


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'curso')
    search_fields = ('matricula', 'nome', 'curso')
    list_filter = ('curso',)
    list_per_page = 15


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'carga_horaria')
    search_fields = ('nome', 'carga_horaria')
    list_filter = ('curso',)
    list_per_page = 15


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('ano', 'turma', 'semestre')
    search_fields = ('ano', 'semestre')
    list_filter = ('ano', 'semestre')
    list_per_page = 15


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'turma', 'data_publicacao', 'data_entrega', 'valor_avaliacao')
    search_fields = ('tipo', 'data_publicacao', 'data_entrega', 'valor_avaliacao')
    list_filter = ('tipo',)
    list_per_page = 15


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('avaliacao', 'turma', 'aluno', 'valor')
    list_per_page = 15


@admin.register(Arquivo)
class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nome_do_arquivo')
    search_fields = ('tipo', 'nome_do_arquivo')
    list_per_page = 15
