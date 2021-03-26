from django.db import models
from decimal import Decimal


class Curso(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descricao', max_length=500)
    carga_horaria = models.IntegerField('Carga Horária')

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome


class Professor(Pessoa):
    OPCOES = (
        ('Doutorado', 'Doutorado'),
        ('Mestrado', 'Mestrado'),
        ('Especialização', 'Especialização'),
        ('Graduação', 'Graduação'),
    )
    titulacao = models.CharField('Titulação', max_length=100, choices=OPCOES)
    curso = models.ForeignKey(Curso, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

class Aluno(Pessoa):
    matricula = models.IntegerField('Matricula', unique=True)
    data_nascimento = models.DateField('Data de nascimento', blank=True, null=True, help_text='Formato DD/MM/AAAA')
    email = models.EmailField('E-mail', blank=True, max_length=200)
    curso = models.ForeignKey(Curso, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

class Disciplina(models.Model):
    curso = models.ForeignKey(Curso, null=True, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=100)
    carga_horaria = models.IntegerField('Carga Horária')
    obrigatoria = models.BooleanField('Obrigatória', default=True)
    ementa = models.TextField('Ementa', blank=True, max_length=500)
    bibliografia = models.TextField('Bibliografia', blank=True, max_length=500)

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

    def __str__(self):
        return self.nome

class Turma(models.Model):
    ano = models.IntegerField('Ano')
    OPCOES = (
        ('1', '.1'),
        ('2', '.2'),
    )
    semestre = models.CharField('Semestre', max_length=2, choices=OPCOES)
    turma = models.CharField('Turma', max_length=10)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, null=True, on_delete=models.SET_NULL)
    alunos = models.ManyToManyField(Aluno)

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

    def __str__(self):
        return f"{self.ano} / {self.semestre} / {self.turma} / {self.disciplina}"

class Arquivo(models.Model):
    OPCOES = (
        ('doc', '.doc'),
        ('pdf', '.pdf'),
    )
    tipo = models.CharField('Tipo', max_length=100, choices=OPCOES)
    nome_do_arquivo = models.FileField('Nome do Arquivo', max_length=100, upload_to='uploads/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'

    def __str__(self):
        return f"{self.nome_do_arquivo} / {self.tipo} / {self.created_at} / {self.updated_at}"


class Avaliacao(models.Model):
    OPCOES = (
        ('Prova', 'Prova'),
        ('Trabalho', 'Trabalho'),
    )
    tipo = models.CharField('Tipo', max_length=20, choices=OPCOES)
    data_publicacao = models.DateField('Data Publicação', help_text='Formato DD/MM/AAAA')
    data_entrega = models.DateField('Data de Entrega', help_text='Formato DD/MM/AAAA')
    # VOLTAR AQUI
    arquivo = models.ForeignKey(Arquivo, null=True, on_delete=models.SET_NULL)
    valor_avaliacao = models.DecimalField('Valor Avaliação', max_digits=5, decimal_places=2)
    turma = models.ForeignKey(Turma, null=True, on_delete=models.SET_NULL)
    orientacoes = models.TextField('Orientações', blank=True, max_length=500)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return f"{self.tipo} / {self.data_publicacao} / {self.data_entrega} / {self.turma} / {self.valor_avaliacao}"

class Nota(models.Model):
    avaliacao = models.ForeignKey(Avaliacao, null=True, on_delete=models.SET_NULL)
    turma = models.ForeignKey(Turma, null=True, on_delete=models.SET_NULL)
    aluno = models.ForeignKey(Aluno, null=True, on_delete=models.SET_NULL)
    valor = models.DecimalField('Nota', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'

    def __str__(self):
        return f"{self.avaliacao} / {self.aluno} / {self.turma} / {self.valor}"


