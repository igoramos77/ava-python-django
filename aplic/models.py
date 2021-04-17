from django.db import models
from django_cryptography.fields import encrypt
from uuid import uuid4
from stdimage import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return filename


#   valida as extensões de arquivos upados no campo foto
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Extensão de arquivo não suportada. Apenas .jpg, .jpeg ou .png')


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
    email = models.EmailField('E-mail', max_length=200)
    senha = encrypt(models.CharField(max_length=50))
    foto = StdImageField(blank=True, null=True, delete_orphans=True, upload_to=get_file_path,
                         variations={'thumbnail': {'width': 128, 'height': 128}}, )
    lattes = models.CharField('Curriculo Lattes', blank=True, null=True, max_length=155)
    facebook = models.CharField('Facebook', blank=True, null=True, max_length=155)
    twitter = models.CharField('Twitter', blank=True, null=True, max_length=155)
    instagram = models.CharField('Instagram', blank=True, null=True, max_length=155)
    linkedin = models.CharField('Linkedin', blank=True, null=True, max_length=155)

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
    curso = models.ForeignKey(Curso, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'


class Disciplina(models.Model):
    curso = models.ForeignKey(Curso, null=True, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=100)
    carga_horaria = models.IntegerField('Carga Horária')
    credito = models.IntegerField('Créditos')
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
    PERIODOS = (
        ('1', '1º'),
        ('2', '2º'),
        ('3', '3º'),
        ('4', '4º'),
        ('5', '5º'),
        ('6', '6º'),
        ('7', '7º'),
        ('8', '8º'),
        ('9', '9º'),
        ('10', '10º'),
        ('11', '11º'),
        ('12', '12º'),
    )
    periodo = models.CharField('Período', max_length=3, choices=PERIODOS)
    turma = models.CharField('Nome da Turma', max_length=10)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, null=True, on_delete=models.SET_NULL)
    DIAS = (
        ('1', 'Domingo'),
        ('2', 'Segunda-feira'),
        ('3', 'Terça-feira'),
        ('4', 'Quarta-feira'),
        ('5', 'Quinta-feira'),
        ('6', 'Sexta-feira'),
        ('7', 'Sábado'),
    )
    dia_da_semana = models.CharField('Dia da Semana', choices=DIAS, max_length=13)
    horario_de_inicio = models.TimeField('Horário de início')
    horario_de_termino = models.TimeField('Horário de término')
    alunos = models.ManyToManyField(Aluno)

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

    def __str__(self):
        return f"{self.turma} / {self.ano} / {self.semestre} / {self.disciplina}"


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
    COMPOSICOES = (
        ('P1', 'P1'),
        ('P2', 'P2'),
        ('P3', 'P3'),
    )
    composicao = models.CharField('Composição', max_length=3, choices=COMPOSICOES)
    data_publicacao = models.DateField('Data Publicação', help_text='Formato DD/MM/AAAA')
    data_entrega = models.DateField('Data de Entrega', help_text='Formato DD/MM/AAAA')
    arquivo = models.FileField('Arquivo')
    valor_avaliacao = models.DecimalField('Valor Avaliação', max_digits=5, decimal_places=2)
    turma = models.ForeignKey(Turma, null=True, on_delete=models.SET_NULL)
    orientacoes = models.TextField('Orientações', blank=True, max_length=500)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return f"{self.tipo} / {self.turma}"


class Nota(models.Model):
    turma = models.ForeignKey(Turma, null=True, on_delete=models.SET_NULL)
    avaliacao = models.ForeignKey(Avaliacao, null=True, on_delete=models.SET_NULL)
    aluno = models.ForeignKey(Aluno, null=True, on_delete=models.SET_NULL)
    valor = models.DecimalField('Nota', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'

    def __str__(self):
        return f"{self.avaliacao} / {self.aluno} / {self.turma} / {self.valor}"
