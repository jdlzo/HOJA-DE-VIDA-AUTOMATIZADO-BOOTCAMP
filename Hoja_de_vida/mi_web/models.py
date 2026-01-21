from django.db import models

# Create your models here.
class DatosPersonales(models.Model):
    idperfil = models.IntegerField(primary_key=True)
    descripcionperfil = models.CharField(max_length=800)
    perfilactivo = models.IntegerField()
    apellidos = models.CharField(max_length=60)
    nombres = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=20)
    lugarnacimiento = models.CharField(max_length=60)
    fechanacimiento = models.DateField()
    numerocedula = models.CharField(max_length=10, unique=True)
    sexo = models.CharField(max_length=1)
    estadocivil = models.CharField(max_length=50)
    licenciaconducir = models.CharField(max_length=6)
    telefonoconvencional = models.CharField(max_length=15)
    telefonofijo = models.CharField(max_length=15)
    direcciontrabajo = models.CharField(max_length=50)
    direcciondomiciliaria = models.CharField(max_length=50)
    sitioweb = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'datospersonales'

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    
class ExperienciaLaboral(models.Model):
    idexperiencialaboral = models.IntegerField(primary_key=True)
    idperfilconqueestaactivo = models.ForeignKey(
        DatosPersonales,
        db_column='idperfilconqueestaactivo',
        on_delete=models.DO_NOTHING,
        related_name='experiencias'
    )
    cargodesempenado = models.CharField(max_length=100)
    nombrempresa = models.CharField(max_length=50)
    lugarempresa = models.CharField(max_length=50)
    emailempresa = models.CharField(max_length=100)
    sitiowebempresa = models.CharField(max_length=100)
    nombrecontactoempresarial = models.CharField(max_length=100)
    telefonocontactoempresarial = models.CharField(max_length=60)
    fechainiciogestion = models.DateField()
    fechafingestion = models.DateField()
    descripcionfunciones = models.CharField(max_length=100)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'experiencialaboral'
class CursosRealizados(models.Model):
    idcursorealizado = models.IntegerField(primary_key=True)
    idperfilconqueestaactivo = models.ForeignKey(
        DatosPersonales,
        db_column='idperfilconqueestaactivo',
        on_delete=models.DO_NOTHING,
        related_name='cursos'
    )
    nombrecurso = models.CharField(max_length=100)
    fechainicio = models.DateField()
    fechafin = models.DateField()
    totalhoras = models.IntegerField()
    descripcioncurso = models.CharField(max_length=100)
    entidadpatrocinadora = models.CharField(max_length=100)
    nombrecontactoauspicia = models.CharField(max_length=100)
    telefonocontactoauspicia = models.CharField(max_length=60)
    emailempresapatrocinadora = models.CharField(max_length=60)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cursosrealizados'
