# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 22:36:59 2016

@author: wilmer
"""

import csv as csv 
import numpy as np
import os
from sklearn import preprocessing
os.getcwd()
os.chdir("/home/wilmer/Escritorio/Tarea1")

data_file = open('data.csv', 'rb')
data_file_object = csv.reader(data_file)
header = data_file_object.next()

data=[]                          
for row in data_file_object:      
    data.append(row[1:])
data = np.array(data)

fechaNacimiento = []
estadoCivil = []
sexo = []
escuela = []
cambioDireccion = []
eficiencia = []
promedio = []
tesis = []
otroBeneficio = []
actividad = []
montoBeca = []
aporte1 = []
aporte2 = []
aporte3 = []
egreso1 = []
egreso2 = []
egreso4 = []
egreso5 = []
egreso6 = []
egreso7 = []
egreso8 = []
egreso9 = []
ingresoR = []
otrosIngresoR = []
egreso11 = []
egreso12 = []
egreso13 = []
egreso14 = []
egreso15 = []
egreso16 = []
egreso17 = []
egreso18 = []
periodo = []

for row in data:
    x = row[2]                              #Columna de Fecha de Nacimiento
    y = row[3]                              #Columna de Edad        
    y = y.split(" ")                        #Si la edad contiene otro dato aporte del numero se separa y nos quedamos con la primera posicion que es la edad
    y = y[0]  
    z = row[5]                              #Columna de Sexo
    estadoCivilRow = row[4]
    escuelaRow = row[6]             
    promedioRow = row[16]                  
    eficienciaRow = row[17]                   
    
    ####Inicio Formato Fecha    
    
    if (x[-1:] == " "):                     # Se elminan espacio en blanco al final de aluna fecha
        x = x.replace(x[-1:],"")
    x = x.replace("-","/")                  # El formato para la fecha sera DD/MM/YYYY
    x = x.replace(" ","/")
    if not (x[-4:].isdigit()):              #Si los ultimos 4 digitos no son numeros
        if (x[-2:].isdigit()):              #Si los ultimos 2 digitos son numeros
            aux = int(x[-2:]) + 1900        #Le sumo 1900 para tener el ano de nacimiento
            x = x.replace(x[-2:],str(aux))
            
    if (x.isdigit()):                       #Si la fecha esta compuesta por puros numeros
        if (len(x) == 8) or (len(x) == 7):
            if (int(x[-4:]) > 1900):        # Si el ano es valido se le agrega el formato
                x = x.replace(x[-4:],"/"+x[-4:])
                x = x.replace(x[-7:-5],"/"+x[-7:-5])
            else:
                x = ""
                
    if not (x[0:2].isdigit()):         # Si el dia esta compuesto por un solo digito
        x = x.replace(x[0:2],"0"+x[0:2])
        
    if not(x[3:5].isdigit()):          # Si el mes esta compuesto por un solo digito
        x = x.replace(x[3:4],"0"+x[3:4])
       
    if (int(x[-4:]) > 2000):                
        if not (x == ""):        
            x = x.replace(x[-4:],str(2015 - int(y)))
    
    fechaNacimiento.append(x)
    
    ####Fin Formato Fecha

    if not ((estadoCivilRow == "Casado (a)") or (estadoCivilRow == "Viudo (a)") or (estadoCivilRow == "Soltero (a)")):
        estadoCivilRow = ""
        
    estadoCivil.append(estadoCivilRow)
    
    
    if (z == "Femenino" ):                  # Se guarda la Estado Civil FInal
        sexo.append("0")
    else:
        sexo.append("1")
        
    if (escuelaRow == "Bioanálisis" ):         # Se guarda la Escuela
        escuela.append("0")
    else:
        escuela.append("1")
        
    cambioDireccionRow = row[10]
    
    if (cambioDireccionRow == "Si"):
        cambioDireccionRow = cambioDireccionRow + ", " + row[11]
    cambioDireccion.append(cambioDireccionRow)
    
    while (float(eficienciaRow) > 1):       
        eficienciaRow = float(eficienciaRow) / 10
    eficiencia.append(eficienciaRow)        # Se guarda la Eficiencia FInal
        
    while (float(promedioRow) > 20):       
        promedioRow = float(promedioRow) / 10
    promedio.append(promedioRow)            # Se guarda la Promedio FInal
    
    tesisRow = row[20]
    if (tesisRow == "Si"):
        tesisRow = tesisRow + ", " + row[21]
    tesis.append(tesisRow)

    otroBeneficioRow = row[29]
    if (otroBeneficioRow == "Si"):
        otroBeneficioRow = otroBeneficioRow + ", " + row[30]
    otroBeneficio.append(otroBeneficioRow)

    actividadRow = row[31]
    if (actividadRow == "Si"):
        actividadRow = actividadRow + ", " + row[32]
    actividad.append(actividadRow)
    
    montoBecaRow = row[33]
    if not (montoBecaRow.isdigit()):
        montoBecaRow = 0
    montoBeca.append(montoBecaRow)

    aporte1Row = row[34]
    if not (aporte1Row.isdigit()):
        aporte1Row = 0
    aporte1.append(aporte1Row)
    
    aporte2Row = row[35]
    if not (aporte2Row.isdigit()):
        aporte2Row = 0
    aporte2.append(aporte2Row)
    
    aporte3Row = row[36]
    if not (aporte3Row.isdigit()):
        aporte3Row = 0
    aporte3.append(aporte3Row)
    
    egreso1Row = row[38]
    if not (egreso1Row.isdigit()):
        egreso1Row = 0
    egreso1.append(egreso1Row)
    
    egreso2Row = row[39]
    if not (egreso2Row.isdigit()):
        egreso2Row = 0
    egreso2.append(egreso2Row)

    egreso3Row = row[40]
    if not (egreso3Row.isdigit()):
        egreso3Row = 0

    egreso4Row = row[41]
    if not (egreso4Row.isdigit()):
        egreso4Row = 0
    egreso4.append(int(egreso3Row)+int(egreso4Row))

    egreso5Row = row[42]
    if not (egreso5Row.isdigit()):
        egreso5Row = 0
    egreso5.append(egreso5Row)

    egreso6Row = row[43]
    if not (egreso6Row.isdigit()):
        egreso6Row = 0
    egreso6.append(egreso6Row)

    egreso7Row = row[44]
    if not (egreso7Row.isdigit()):
        egreso7Row = 0
    egreso7.append(egreso7Row)

    egreso8Row = row[45]
    if not (egreso8Row.isdigit()):
        egreso8Row = 0
    egreso8.append(egreso8Row)

    egreso9Row = row[46]
    if not (egreso9Row.isdigit()):
        egreso9Row = 0
    egreso9.append(egreso9Row)
    
    ingresoRRow = row[50]
    ingresoRRow = ingresoRRow.replace(" ","")
    ingresoRRow = ingresoRRow.replace(",",".")
    ingresoRRow = ingresoRRow.replace("bs","")
    if not (ingresoRRow.isdigit()):
        aux = ingresoRRow.split(".")
        if (len(aux) > 2):
           ingresoRRow = aux[0] + aux[1] + "." + aux[2] 
        else:
            if(len(aux) == 2):
                if(len(aux[1]) > 2):
                    ingresoRRow = aux[0] + aux[1]
            else:
                ingresoRRow = 0       
    ingresoR.append(ingresoRRow)
    
    otrosIngresoRRow = row[51]
    otrosIngresoRRow = otrosIngresoRRow.replace(" ","")
    otrosIngresoRRow = otrosIngresoRRow.replace(",",".")
    otrosIngresoRRow = otrosIngresoRRow.replace("bs","")
    if not (otrosIngresoRRow.isdigit()):
        aux =  otrosIngresoRRow.split(".")
        if (len(aux) == 1):
            otrosIngresoRRow = 0
    otrosIngresoR.append(otrosIngresoRRow) 
    
    egreso11Row = row[53]    
    egreso11Row = egreso11Row.replace(" ","")
    egreso11Row = egreso11Row.replace(",",".")
    egreso11Row = egreso11Row.replace("bs","")
    if not (egreso11Row.isdigit()):
        aux = egreso11Row.split(".")
        if (len(aux) > 2):
           egreso11Row = aux[0] + aux[1] + "." + aux[2] 
        else:
            if(len(aux) == 2):
                if(len(aux[1]) > 2):
                    egreso11Row = aux[0] + aux[1]
            else:
                egreso11Row = 0       
    egreso11.append(egreso11Row)
    
    egreso12Row = row[54]    
    egreso12Row = egreso12Row.replace(" ","")
    egreso12Row = egreso12Row.replace(",",".")
    egreso12Row = egreso12Row.replace("bs","")
    if not (egreso12Row.isdigit()):
        aux = egreso12Row.split(".")
        if (len(aux) > 2):
           egreso12Row = aux[0] + aux[1] + "." + aux[2] 
        else:
            if(len(aux) == 2):
                if(len(aux[1]) > 2):
                    egreso12Row = aux[0] + aux[1]
            else:
                egreso12Row = 0       
    egreso12.append(egreso12Row)
    
    egreso13Row = row[55]    
    egreso13Row = egreso13Row.replace(" ","")
    egreso13Row = egreso13Row.replace(",",".")
    egreso13Row = egreso13Row.replace("bs","")
    if not (egreso13Row.isdigit()):
        aux = egreso13Row.split(".")
        if (len(aux) > 2):
           egreso13Row = aux[0] + aux[1] + "." + aux[2] 
        else:
            if(len(aux) == 2):
                if(len(aux[1]) > 2):
                    egreso13Row = aux[0] + aux[1]
            else:
                egreso13Row = 0       
    egreso13.append(egreso13Row)
    
    egreso14Row = row[56]    
    egreso14Row = egreso14Row.replace(" ","")
    egreso14Row = egreso14Row.replace(",",".")
    egreso14Row = egreso14Row.replace("bs","")
    if not (egreso14Row.isdigit()):
        aux = egreso14Row.split(".")
        if (len(aux) > 2):
           egreso14Row = aux[0] + aux[1] + "." + aux[2] 
        else:
            if(len(aux) == 2):
                if(len(aux[1]) > 2):
                    egreso14Row = aux[0] + aux[1]
            else:
                egreso14Row = 0
                
    egreso15Row = row[57]    
    egreso15Row = egreso15Row.replace(" ","")
    egreso15Row = egreso15Row.replace(",",".")
    egreso15Row = egreso15Row.replace("bs","")
    if not (egreso15Row.isdigit()):
        aux = egreso15Row.split(".")
        if (len(aux) > 2):
           egreso15Row = aux[0] + aux[1] + "." + aux[2] 
        else:
            if(len(aux) == 2):
                if(len(aux[1]) > 2):
                    egreso15Row = aux[0] + aux[1]
            else:
                egreso15Row = 0           
                
    egreso14.append(float(egreso14Row)+float(egreso14Row))
    
    
    egreso15Row = row[58]
    if not (egreso15Row.isdigit()):
        egreso15Row = 0
    egreso15.append(egreso15Row)

    egreso16Row = row[59]
    if not (egreso16Row.isdigit()):
        egreso16Row = 0
    egreso16.append(egreso16Row)
    
    egreso17Row = row[60]    
    egreso17Row = egreso17Row.replace(" ","")
    egreso17Row = egreso17Row.replace(",",".")
    egreso17Row = egreso17Row.replace("bs","")
    if not (egreso17Row.isdigit()):
        aux = egreso17Row.split(".")
        if (len(aux) > 2):
           egreso17Row = aux[0] + aux[1] + "." + aux[2] 
        else:
            if(len(aux) == 2):
                if(len(aux[1]) > 2):
                    egreso17Row = aux[0] + aux[1]
            else:
                egreso17Row = 0       
    egreso17.append(egreso17Row)
    
    egreso18Row = row[60]    
    egreso18Row = egreso18Row.replace(" ","")
    egreso18Row = egreso18Row.replace(",",".")
    egreso18Row = egreso18Row.replace("bs","")
    if not (egreso18Row.isdigit()):
        aux = egreso18Row.split(".")
        if (len(aux) > 2):
           egreso18Row = aux[0] + aux[1] + "." + aux[2] 
        else:
            if(len(aux) == 2):
                if(len(aux[1]) > 2):
                    egreso18Row = aux[0] + aux[1]
            else:
                egreso18Row = 0       
    egreso18.append(egreso18Row)

    periodoRow = row[0]
    if(periodoRow.find("2014")):
        periodoRow = "2014"
    else:
        if(periodoRow.find("2015")):
            periodoRow = "2015"
        else:
            periodoRow ="0"
    periodo.append(periodoRow)

data[0::,0] = np.array(periodo)
data[0::,2] = np.array(fechaNacimiento)
data[0::,4] = np.array(estadoCivil)
data[0::,5] = np.array(sexo)
data[0::,6] = np.array(escuela)
data[0::,10] = np.array(cambioDireccion)
data[0::,16] = np.array(promedio)
data[0::,17] = np.array(eficiencia)   
data[0::,20] = np.array(tesis)      
data[0::,29] = np.array(otroBeneficio)
data[0::,31] = np.array(actividad)
data[0::,33] = np.array(montoBeca)
data[0::,34] = np.array(aporte1)
data[0::,35] = np.array(aporte2)
data[0::,36] = np.array(aporte3)
data[0::,38] = np.array(egreso1)
data[0::,39] = np.array(egreso2)
data[0::,41] = np.array(egreso4)
data[0::,42] = np.array(egreso5)
data[0::,43] = np.array(egreso6)
data[0::,44] = np.array(egreso7)
data[0::,45] = np.array(egreso8)
data[0::,46] = np.array(egreso9)
data[0::,50] = np.array(ingresoR)
data[0::,51] = np.array(otrosIngresoR)
data[0::,53] = np.array(egreso11)
data[0::,54] = np.array(egreso12)
data[0::,55] = np.array(egreso13)
data[0::,56] = np.array(egreso14)
data[0::,58] = np.array(egreso15)
data[0::,59] = np.array(egreso16)
data[0::,60] = np.array(egreso17)
data[0::,61] = np.array(egreso18)
minable_file = open("minable.csv", "wb")
minable_file_object = csv.writer(minable_file)

minable_file_object.writerow(["AñoRenovacionDeBeca", "CI", "FNacimiento", "EstadoCivil", "Sexo", "Escuela", "AñoIngresoUCV", "ModalidadIngresoUCV", "SemestreQueCursa", "CambiadoDireccion","#MateriasInscritasSemestreOAñoAnterior", "#MateriasAprobadasSemestreOAñoAnterior", "#MateriasRetiradasSemestreOAñoAnterior", "#MateriasReprobadasSemestreOAñoAnterior", "PromedioPonderadoAprobado", "Eficiencia", "#MateriasInscritasActual", "Tesis.TrabajoDeGrado.Pasantías", "Procedencia", "LugarResidencia", "Personas.con.las.cuales.usted.vive..mientras.estudia.en.la.universidad", "Tipo.de.vivienda.donde.reside.mientras.estudia.en.la.universidad", "X.Ha.solicitado.algún.otro.beneficio.a.la.Universidad.u.otra.Institución.", "X.Se.encuentra.usted..realizando.alguna.actividad.que.le.genere.ingresos.", "MontoBeca",
"Aporte.mensual.que.le.brinda.su.responsable.económico", "Aporte.mensual.que.recibe.de.familiares.o.amigos", "Ingreso.mensual.que.recibe.por.actividades.a.destajo.o.por.horas", "Alimentacion", "Transporte", "GastosMedicos","GastosPersonales", "Residencia", "MaterialEstudio","Recreacion", "OtrosGastos", "ResponsableEconomico", "CargasFamiliares", "Ingreso.mensual.de.su.responsable.económico", "OtrosIngresos", "Vivienda", "Alimentacion2","Transporte2", "GastosMedicos2", "GastosEducativos" ,"ServicioPublicos", "Condominio", "OtrosGastos2",
"Deseamos.conocer.la.opinión.de.nuestros.usuarios..para.mejorar.la.calidad.de.los.servicios.ofrecidos.por.el.Dpto..de.Trabajo.Social.OBE", "Sugerencias.y.recomendaciones.para.mejorar.nuestra.atención"])

for row in data:  
    minable_file_object.writerow(np.concatenate((row[0:3], row[4:11], row[12:18], row[19:21], row[22:26],row[29:30],row[31:32],row[33:37], row[38:40], row[41:47], row[48:52], row[53:57],row[58:62],row[63:65] ), axis = 0))
    
minable_file.close()
data_file.close()
