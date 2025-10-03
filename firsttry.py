
def validEntero(numero,text):
    while True:
        try:
            numero=int(input('texto'))
            if (opcion>0 and opcion<= numero):
                break
            else:
                print("Que parte de numero entre 1 y", numero,"no entendiste")
        except ValueError:
            print("Que parte de numero no entendiste???")

    return opcion


def validDecimal(texto):
    while True:
        try:
            opcion=float(input('texto'))
            if (opcion>0):
                break
            else:
                print("Que parte de numero amyr que 0 no entendiste")
        except ValueError:
            print("Que parte de numero no entendiste???")
    return opcion

def validSexo(texto):
    opcion=input(texto).strip().upper()
    if opcion!='M' and opcion!='F':
        opcion='OTRO'
    return opcion



def altaPaciente(pacientes):
    id_paciente= validEntero(500,'Dame le id del paciente')
    if id_paciente in pacientes:
        print("Ese id ya existe")
        return pacientes
    #datos personales
    nombre=input("Nombre")
    edad=validEntero(120,'Edad: ')
    sexo=validSexo('Sexo (M / F / OTRO): ')
    #datos signos vitales
    peso= validDecimal('Dame el peso: ')
    altura=validDecimal('Dame la altura: ')
    presionS=validEntero(300,'Dame la presion Sistolica: ')
    presionD=validEntero(300,'Dame la presion Distolica: ')
    #datos especiales
    alergias=input('Alergias: ')
    religion=input('Relgion: ')
    sangre=input('Sangre: ')
    #Equipo medico
    doctor=input('Medico: ')
    enfermeros=input('Enfermeros: ')
    guardia=input('Guardias: ')
    sala=input('Sala de operaciones: ')
    #notas
    notas=input('Notas: ')

    pacientes[id_paciente]={'Datos Peronsales':{'Nombre':nombre,'Edad':edad,'Sexo':sexo}, 
    'Signos Vitales':{'Peso':peso,'Altura':altura,'Sistolica':presionS,'Distolica':presionD},
    'Datos Especiales':{'Alergia':alergias,'Religion':religion,'Sangre':sangre},
    'Hospital':{'Medico':doctor,'Enfermeros':enfermeros,'Guardias':guardia,'Sala de operaciones':sala,
    'Notas':notas }}

#programa principal


pacientes={}
while True:
    print("\n-----Sistema de control de pacientes-------")
    print("1,Alta de paciente")
    print("2,Baja de paciente")
    print("3,Cambio de paciente")
    print("4,Ver expediente del paciente")
    print("5,salir")

    opcion= validEntero(5,'Eligue la opcion deseada: ')

    if opcion==1:
        pacientes=altaPaciente(pacientes)
    elif opcion==2:
        bajaPaceinte(pacientes)
    elif opcion==3:
        cambioPaceinte(pacientes)
    elif opcion==4:
        expedientePaceinte(pacientes)
    else:
        break





