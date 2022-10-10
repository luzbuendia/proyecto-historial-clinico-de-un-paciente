from django.db import models

# Create your models here.
class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Medico(models.Model):
    idMedico = models.CharField(max_length=20)
    nombre =  models.CharField(max_length=50)
    apellido = models.CharField(max_length=50) 
    especialidad = models.ForeignKey(Especialidad,on_delete=models.CASCADE,blank=True,default='')    
    numeroDeColeg = models.CharField(max_length=30)
    telefono =  models.CharField(max_length=15)
    email =  models.CharField(max_length=50)
    def __str__(self):
        return self.idMedico +' '+self.nombre +' '+self.apellido +' '+str(self.especialidad) +' '+self.numeroDeColeg +' '+self.telefono+''+self.email

class Paciente(models.Model):
    idSeguridadSocial = models.CharField(max_length=15)
    nombre =  models.CharField(max_length=50)
    apellido = models.CharField(max_length=50) 
    dni = models.CharField(max_length=12)
    fechaDeNacimiento = models.CharField(max_length=13)
    sexo =  models.CharField(max_length=15)
    domicilio =  models.CharField(max_length=50)
    telefono =  models.CharField(max_length=15)
    provincia =  models.CharField(max_length=50)
    def __str__(self):
        return self.idSeguridadSocial+'-'+self.nombre +'-'+self.apellido +'-'+self.dni+ '-'+ self.fechaDeNacimiento +'-'+self.sexo +'-'+self.domicilio +'-'+self.telefono+'-'+self.provincia

class Servicio(models.Model):
    nombreServi = models.CharField(max_length=50)
    def __str__(self):
        return self.nombreServi

class Cita(models.Model):
    idCita = models.CharField(max_length=30)
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE) 
    servicio = models.ForeignKey(Servicio,on_delete=models.CASCADE,blank=True,default='')
    fecha = models.CharField(max_length=30)
    hora =  models.CharField(max_length=6)
    medico = models.ForeignKey(Medico,on_delete=models.CASCADE) 
    def __str__(self):
        return self.idCita +'-'+str(self.paciente.nombre)+''+ str(self.paciente.apellido)+'-'+str(self.servicio) +'- '+self.fecha+'- '+ self.hora +'-'+str(self.medico.nombre)+''+str(self.medico.apellido)

class Enfermera(models.Model):
    nombre= models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Triaje(models.Model):
    enfermera = models.ForeignKey(Enfermera,on_delete=models.CASCADE,blank=True,default='') 
    paciente =  models.ForeignKey(Paciente,on_delete=models.CASCADE)
    def __str__(self):
        return  str(self.enfermera)+'-' +str(self.paciente.nombre)

class Historia(models.Model):
    idHistorial = models.CharField(max_length=25)
    paciente =  models.ForeignKey(Paciente,on_delete=models.CASCADE)
    fecha = models.CharField(max_length=30)
    observacion = models.CharField(max_length=100)
    def __str__(self):
        return self.idHistorial +' '+str(self.paciente)+' '+self.fecha +' '+self.observacion


class Medicamento(models.Model):
    idMedicamento= models.CharField(max_length=20)
    nombrMedicamento = models.CharField(max_length=20)
    cantidad = models.CharField(max_length=20)
    def __str__(self):
        return self.idMedicamento +' '+ self.nombrMedicamento+' '+self.cantidad


class Tratamiento(models.Model):
    idTratamiento = models.CharField(max_length=30)
    cirugia= models.CharField(max_length=50)
    medicamento= models.ForeignKey(Medicamento,on_delete=models.CASCADE)
    dieta = models.CharField(max_length=100)
    terapia = models.CharField(max_length=50)
    rehabilitacion = models.CharField(max_length=40) 
    radioTerapia = models.CharField(max_length=25)
    def __str__(self):
        return self.idTratamiento +'- '+self.cirugia +'- '+str(self.medicamento.nombrMedicamento)+'- '+self.dieta+'- '+ self.terapia +'- '+self.rehabilitacion +' -'+self.radioTerapia

class Enfermedad(models.Model):
    nombreEnfer = models.CharField(max_length=50)  
    def __str__(self):
        return self.nombreEnfer

class Diagnostico(models.Model):
    idDiagnostico = models.CharField(max_length=30)
    sintomas=  models.CharField(max_length=50)
    dolor = models.CharField(max_length=100)
    tiempo = models.CharField(max_length=20)
    enfermedad = models.ForeignKey(Enfermedad,on_delete=models.CASCADE,blank=True,default='')
    def __str__(self):
        return self.idDiagnostico+'- '+self.sintomas+'- '+self.dolor +'- '+self.tiempo+' -'+str(self.enfermedad)


class Atencion(models.Model):
    idAtencion = models.CharField(max_length=50)
    triaje= models.ForeignKey(Triaje,on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(Tratamiento,on_delete=models.CASCADE)
    historia = models.ForeignKey(Historia,on_delete=models.CASCADE)
    diagnostico = models.ForeignKey(Diagnostico,on_delete=models.CASCADE)
    def __str__(self):
        return self.idAtencion +' -'+str(self.triaje)+' -'+str(self.tratamiento)+' -'+str(self.historia)+' -'+str(self.diagnostico)

    
class ResetaMedica(models.Model):
    idResetaMedica= models.CharField(max_length=100)
    tratamiento = models.ForeignKey(Tratamiento,on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento,on_delete=models.CASCADE)
    dosis = models.CharField(max_length=20)
    dia = models.CharField(max_length=20)
    hora =models.CharField(max_length=30)
    def __str__(self):
        return self.idResetaMedica+' -'+str(self.tratamiento.dieta)+' -'+str(self.medicamento.nombrMedicamento)+' -'+self.dosis+' -'+ self.dia +' -'+self.hora


    
 




    
