import requests
import json
from datetime import date
from datetime import datetime
from faker import Faker
from faker.providers import DynamicProvider

faker = Faker('es')

tecnologia_provider = DynamicProvider(provider_name="tecnologia",elements=["PHP","Node.js","Java","TypeScript","Python","Ruby","GraphQL","CFML","Erlang","Adobe Flash","django","ASP.NET", "Pascal", "C++"],)
faker.add_provider(tecnologia_provider)

clasificacion_incidente_provider = DynamicProvider(provider_name="clasificacion_incidente",elements=["Denegación de servicio (DoS)","Malware","Phishing","Ransomware","Ataques de intermediario (MITM)","Ataques de fuerza bruta","Inyección SQL","Secuencias de comandos entre sitios (XSS)","Falsificación de solicitudes entre sitios (CSRF)","Desbordamiento de búfer",
"Falsificación de solicitudes entre sitios (XSRF)","Ataque de sesión","Desfiguración",],)
faker.add_provider(clasificacion_incidente_provider)


url_uci_provider = DynamicProvider(provider_name="url_incidente",elements=["https://firefoxmania.example.com/tag/launching/page/15/", 
                                                                           "https://humanos.example.com/search/Hacking/page/4/",
                                                                           "http://coj.example.com/24h/status.xhtml?",
                                                                           "https://cjc-forum.example.com/",
                                                                           "http://humanos.example.com/feed/",
                                                                           "https://coj.example.com/24h/status.xhtml?",
                                                                           "https://coj.example.com/tables/status.xhtml?",
                                                                           "https://coj-forum.example.com/viewtopic.php?",
                                                                           "https://coj.example.com/contest/cproblem.xhtml?",
                                                                           "http://firefoxmania.example.com/robots.txt",
                                                                           "http://coj-forum.example.com/robots.txt",
                                                                           "http://humanos.example.com/robots.txt",
                                                                           "http://composer.prod.example.com/robots.txt",
                                                                           "http://publicaciones.example.com/robots.txt",
                                                                           "http://www.example.com/robots.txt",
                                                                           "http://coj.example.com/robots.txt",
                                                                           "http://developer.firefoxmania.example.com/robots.txt",
                                                                           "http://rcci.example.com/robots.txt",
                                                                           "https://humanos.example.com/question/hackear-contrasena-a-ficheros-isz/",
                                                                           "https://coj.example.com/24h/status.xhtml?",
                                                                           "https://doc.example.com/status.xhtml?",
                                                                           "https://humanos.example.com/search/liberaci%C3%B3n/page/5/",
                                                                           "https://coj.example.com/js/countdown.js","http://correo.example.com/","https://coj.example.com/tables/status.xhtml?",
                                                                           "https://firefoxmania.example.com/category/eventos/page/17/","https://coj-forum.example.com/viewtopic.php?","http://coj.example.com/contest/cstatus.xhtml?",
                                                                           "https://coj.example.com/24h/status.xhtml?","https://coj.example.com/js/countdown.js","https://coj.example.com/tables/status.xhtml?","http://coj.example.com/24h/status.xhtml?","https://firefoxmania.example.com/category/soluciones/page/26/","http://coj.example.com/tables/status.xhtml?","http://coj.example.com/tables/cstatus.xhtml?","http://127.0.0.1/cgi-bin/ViewLog.asp","https://coj.example.com/24h/status.xhtml?","https://humanos.example.com/2012/06/04/blender-en-tu-idioma/","https://www.example.com/sites/default/files/js/js_WAFAbSVWCwdz9jMb0weJVneQwiyLPk9JbS-SUvys_EM.js","https://coj.example.com/tables/status.xhtml?",
                                                                           "https://coj.example.com/24h/status.xhtml?","https://humanos.example.com/feed/","https://www.example.com/sites/default/files/imagenes/noticias/la-citec-inicia-su-festival-1.jpg","https://firefoxmania.example.com/2011/04/29/","http://coj.example.com/24h/status.xhtml?","https://humanos.example.com/2015/04/28/flisol-2015-una-edicion-sin-precedentes/","https://coj.example.com/tables/status.xhtml?","http://www.example.com/en/university/news/practical-contribution-improve-web-portals","http://coj.example.com/tables/status.xhtml?","https://firefoxmania.example.com/category/los-martes-de-firefox/page/4/","https://coj.example.com/24h/problem.xhtml?","http://coj.example.com/24h/status.xhtml?","https://coj.example.com/contest/contestview.xhtml?","https://humanos.example.com/feed","https://humanos.example.com/feed/","http://coj.example.com/24h/problem.xhtml?","http://piwik.example.com/piwik.php?","https://coj.example.com/24h/status.xhtml?","http://coj.example.com/24h/submit.xhtml?","http://piwik.example.com/piwik.php?","http://coj.example.com/24h/submit.xhtml?","http://coj.example.com/24h/status.xhtml","http://coj.example.com/24h/status.xhtml?","http://piwik.example.com/piwik.php?","http://coj.example.com/tables/status.xhtml?","http://coj.example.com/24h/status.xhtml","http://coj.example.com/24h/status.xhtml","http://piwik.example.com/piwik.php?","http://coj.example.com/tables/status.xhtml?","http://coj.example.com/images/coj_favicon.png",],)

faker.add_provider(url_uci_provider)


incidente_provider = DynamicProvider(provider_name="incidente",elements=["Desfiguración del portal web", "Uso del servidor web para criptominería", "Inyección de código mediante la subida de archivos", "Ataque de fuerza bruta contra panel de autenticación", "Desconfiguración del servidor web", "Caída del servidor de base de datos",],)
faker.add_provider(incidente_provider)

pais_provider = DynamicProvider(provider_name="pais",elements=["2","4","30",],)
faker.add_provider(pais_provider)

headers = {
  'Content-Type': 'application/json'
}

"""
url = "http://127.0.0.1:8000/incidente/tecnologia/"

for i in range(20):
    payload = json.dumps({"tecnologia": faker.tecnologia()})
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


url = "http://127.0.0.1:8000/incidente/clasificacionincidente/"
for i in range(20):
    payload = json.dumps({"clasificacion_incidente": faker.clasificacion_incidente()})
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


url = "http://127.0.0.1:8000/incidente/entidad/"
for i in range(50):
    payload = json.dumps({"entidad": faker.company()})
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

url = "http://127.0.0.1:8000/ip/pais/"
for i in range(2):
    payload = json.dumps({"pais": faker.country()})
    response = requests.request("POST", url, headers=headers, data=payload)
    print(id)

url = "http://127.0.0.1:8000/peticion/url/"
for i in range(50):
    payload = json.dumps({"url": faker.url_incidente()})
    response = requests.request("POST", url, headers=headers, data=payload)
    print(id)

url = "http://127.0.0.1:8000/peticion/metodoHTTP/"
for i in range(50):
    payload = json.dumps({"metodo_HTTP": faker.http_method()})
    response = requests.request("POST", url, headers=headers, data=payload)
    print(id)

url = "http://127.0.0.1:8000/peticion/codigorespuestahttp/"
for i in range(50):
    payload = json.dumps({"codigo_respuesta_HTTP": str(faker.random_int(min=100,max=599))})
    response = requests.request("POST", url, headers=headers, data=payload)
    print(id)


url = "http://127.0.0.1:8000/peticion/agenteusuario/"
for i in range(50):
    payload = json.dumps({"agente_usuario": faker.user_agent()})
    response = requests.request("POST", url, headers=headers, data=payload)
    print(id)

url = "http://127.0.0.1:8000/peticion/referencia/"
for i in range(50):
    payload = json.dumps({"referencia": faker.url()})
    response = requests.request("POST", url, headers=headers, data=payload)
    print(id)
"""


url = "http://127.0.0.1:8000/ip/direccionip/listcreate/"
for i in range(50):
    payload = json.dumps({"direccion_IP": faker.unique.ipv4(),
                          "pais": str(faker.random_int(min=17,max=30))})
    response = requests.request("POST", url, headers=headers, data=payload)
    print(id)


url = "http://127.0.0.1:8000/peticion/peticion/"
for i in range(50):
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    payload = json.dumps(
        {
    "fecha": date_time_str,
    "hash_peticion": str(faker.random_int(min=1,max=599999)),
    "direccion_IP": str(faker.random_int(min=7,max=40)),
    "metodo_HTTP":str(faker.random_int(min=1,max=6)),
    "codigo_respuesta_HTTP": str(faker.random_int(min=1,max=6)),
    "agente_usuario": str(faker.random_int(min=1,max=100)),
    "referencia": str(faker.random_int(min=1,max=100)),
    "url": str(faker.random_int(min=1,max=45)),
    "incidente": str(faker.random_int(min=1,max=4)),
}
    )
    response = requests.request("POST", url, headers=headers, data=payload)
    print(id)

url = "http://127.0.0.1:8000/incidente/incidente/listcreate/"
for i in range(10):
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    payload = json.dumps({"nombre_corto": faker.texts(nb_texts=10),
                          "fecha":  date_time_str,
                          "descripcion": faker.texts(nb_texts=10),
                          "tecnologia": str(faker.random_int(min=27,max=40)),
                          "clasificacion_incidente": str(faker.random_int(min=1,max=13)),
                          "entidad": str(faker.random_int(min=537,max=538))})
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

