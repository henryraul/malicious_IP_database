from django.shortcuts import redirect, render
from modulos.ip.models import DireccionIP, Pais
from modulos.peticion.models import MetodoHTTP, CodigoRespuestaHTTP, AgenteUsuario,  URL, Peticion
from modulos.incidente.models import Incidente, ClasificacionIncidente, Tecnologia
from django.contrib.auth import logout


def graficas(request):
    limite = 10
    paises = Pais.objects.all()
    direccionesip = DireccionIP.objects.all()
    top_paises = [['', 0],]
    for pais in paises:
        direccionesip_filter = DireccionIP.objects.filter(pais=pais.id)
        count = 0
        for dirip in direccionesip_filter:
            count = count + \
                Peticion.objects.filter(direccion_IP=dirip.id).count()

        pais_aux = [pais.pais, count]

        condicion = True
        indice = 0
        while (condicion):
            if top_paises[indice][1] < pais_aux[1]:
                top_paises.insert(indice, pais_aux)
                condicion = False
            else:
                indice = indice + 1
                condicion = indice < len(top_paises)
        if indice == len(top_paises):
            top_paises.append(pais_aux)

    label_paises = []
    data_paises = []

    for indice in range(10):
        label_paises.append(top_paises[indice][0])
        data_paises.append(top_paises[indice][1])

    urls = URL.objects.all()
    top_urls_atacadas = [['', 0],]
    for url in urls:
        count = Peticion.objects.filter(url=url.id).count()
        url_aux = [url.url, count]
        condicion = True
        indice = 0
        while (condicion):
            if top_urls_atacadas[indice][1] < url_aux[1]:
                top_urls_atacadas.insert(indice, url_aux)
                condicion = False
            else:
                indice = indice + 1
                condicion = indice < len(top_urls_atacadas)
        if indice == len(top_urls_atacadas):
            top_urls_atacadas.append(url_aux)

    label_url = []
    data_url = []
    for indice in range(10):
        label_url.append(top_urls_atacadas[indice][0])
        data_url.append(top_urls_atacadas[indice][1])

    top_direccionesIP_atacantes = [['', 0],]
    for dirip in direccionesip:
        count = Peticion.objects.filter(direccion_IP=dirip.id).count()
        dirip_aux = [dirip.direccion_IP, count]
        condicion = True
        indice = 0
        while (condicion):
            if top_direccionesIP_atacantes[indice][1] < dirip_aux[1]:
                top_direccionesIP_atacantes.insert(indice, dirip_aux)
                condicion = False
            else:
                indice = indice + 1
                condicion = indice < len(top_direccionesIP_atacantes)
        if indice == len(top_direccionesIP_atacantes):
            top_direccionesIP_atacantes.append(dirip_aux)

    label_dirip = []
    data_dirip = []
    for indice in range(10):
        label_dirip.append(top_direccionesIP_atacantes[indice][0])
        data_dirip.append(top_direccionesIP_atacantes[indice][1])

    clasificacion = ClasificacionIncidente.objects.all()
    top_clasificacion_incidentes = [['', 0],]
    for clasif in clasificacion:
        count = Incidente.objects.filter(
            clasificacion_incidente=clasif.id).count()
        clasif_aux = [clasif.clasificacion_incidente, count]
        condicion = True
        indice = 0
        while (condicion):
            if top_clasificacion_incidentes[indice][1] < clasif_aux[1]:
                top_clasificacion_incidentes.insert(indice, clasif_aux)
                condicion = False
            else:
                indice = indice + 1
                condicion = indice < len(top_clasificacion_incidentes)
        if indice == len(top_clasificacion_incidentes):
            top_clasificacion_incidentes.append(clasif_aux)

    label_clasificacion = []
    data_clasificacion = []
    for indice in range(10):
        label_clasificacion.append(top_clasificacion_incidentes[indice][0])
        data_clasificacion.append(top_clasificacion_incidentes[indice][1])

    tecnologia = Tecnologia.objects.all()
    top_tecnologia_incidentes = [['', 0],]
    for tecno in tecnologia:
        count = Incidente.objects.filter(tecnologia=tecno.id).count()
        tecno_aux = [tecno.tecnologia, count]
        condicion = True
        indice = 0
        while (condicion):
            if top_tecnologia_incidentes[indice][1] < tecno_aux[1]:
                top_tecnologia_incidentes.insert(indice, tecno_aux)
                condicion = False
            else:
                indice = indice + 1
                condicion = indice < len(top_tecnologia_incidentes)
        if indice == len(top_tecnologia_incidentes):
            top_tecnologia_incidentes.append(tecno_aux)

    label_tecnologia = []
    data_tecnologia = []
    for indice in range(6):
        label_tecnologia.append(top_tecnologia_incidentes[indice][0])
        data_tecnologia.append(top_tecnologia_incidentes[indice][1])

    metodosHTTP = MetodoHTTP.objects.all()
    top_metodosHTTP = [['', 0],]
    for metodo in metodosHTTP:
        count = Peticion.objects.filter(metodo_HTTP=metodo.id).count()
        metodo_aux = [metodo.metodo_HTTP, count]
        condicion = True
        indice = 0
        while (condicion):
            if top_metodosHTTP[indice][1] < metodo_aux[1]:
                top_metodosHTTP.insert(indice, metodo_aux)
                condicion = False
            else:
                indice = indice + 1
                condicion = indice < len(top_metodosHTTP)
        if indice == len(top_metodosHTTP):
            top_metodosHTTP.append(metodo_aux)

    label_metodoHTTP = []
    data_metodoHTTP = []
    for indice in range(6):
        label_metodoHTTP.append(top_metodosHTTP[indice][0])
        data_metodoHTTP.append(top_metodosHTTP[indice][1])

    peticiones = Peticion.objects.all().order_by('-id')[:200]

    agente_usuario = set()
    codigo_respuesta_HTTP = set()

    for p in peticiones:

        if len(agente_usuario) < limite:
            agente_usuario.add(p.agente_usuario)
        if len(codigo_respuesta_HTTP) < limite:
            codigo_respuesta_HTTP.add(p.codigo_respuesta_HTTP)

    data = {
        'label_paises': label_paises,
        'data_paises': data_paises,
        'label_url': label_url,
        'data_url': data_url,
        'label_dirip': label_dirip,
        'data_dirip':  data_dirip,
        'label_clasificacion': label_clasificacion,
        'data_clasificacion': data_clasificacion,
        'label_tecnologia': label_tecnologia,
        'data_tecnologia': data_tecnologia,
        'label_metodoHTTP': label_metodoHTTP,
        'data_metodoHTTP': data_metodoHTTP,

    }
    return render(request, 'estadisticas_generales.html', data)


def inicio(request):
    limite = 10
    peticiones = Peticion.objects.all().order_by('-id')[:200]

    paises = set()
    direccionesip = set()
    urls = set()
    metodoshttp = set()
    agente_usuario = set()
    codigo_respuesta_HTTP = set()

    for p in peticiones:
        if len(paises) < limite:
            paises.add(p.direccion_IP.pais)
        if len(direccionesip) < limite:
            direccionesip.add(p.direccion_IP)
        if len(urls) < limite:
            urls.add(p.url)
        if len(metodoshttp) < limite:
            metodoshttp.add(p.metodo_HTTP)
        if len(agente_usuario) < limite:
            agente_usuario.add(p.agente_usuario)
        if len(codigo_respuesta_HTTP) < limite:
            codigo_respuesta_HTTP.add(p.codigo_respuesta_HTTP)

    data = {
        'direccionesip': direccionesip,
        'total_dirIP': DireccionIP.objects.all().count(),
        'paises': paises,
        'totalpaises': Pais.objects.all().count(),
        'urls': urls,
        'totalurl': URL.objects.all().count(),
        'metodoshttp': metodoshttp,
        'totalmetodoshttp': MetodoHTTP.objects.all().count(),
        'agente_usuario': agente_usuario,
        'totalagente_usuario': AgenteUsuario.objects.all().count(),
        'codigo_respuesta_HTTP': codigo_respuesta_HTTP,
        'totalcodigo_respuesta_HTTP': CodigoRespuestaHTTP.objects.all().count(),
    }
    return render(request, 'estadistica_ataques_recientes.html', data)


def contacto(request):
    return render(request, 'contacto.html')

def buscar(request):
    cantidad_peticiones = 0
    lista_incidentes = set()
    mensajeid = 0
    mensaje = "La dirección IP es incorrecta"
    try:
        buscarip = request.GET.get('busqueda')
        if buscarip:
            dirip = DireccionIP.objects.filter(direccion_IP=buscarip).first()
            
            if dirip:
                mensaje = 'La dirección IP se encuentra en la base de datos'
                mensajeid = 1
                peticiones = Peticion.objects.filter(direccion_IP=dirip.id)
                cantidad_peticiones = peticiones.count()
                for peticion in peticiones:
                    
                    if not (peticion.incidente in lista_incidentes):                       
                        lista_incidentes.add(peticion.incidente)
            else:
                mensaje = 'La dirección IP no se encuentra en la base de datos'
                mensajeid = 2
    except:
        mensaje = "Error"

    data = {
        'mensaje': mensaje,
        'mensajeid' :  mensajeid,
        'lista_incidentes': lista_incidentes,
        'cantidad_peticiones': cantidad_peticiones,
        }
    return render(request, 'buscar.html', data)



