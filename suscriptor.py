import redis

# Conexión a Redis con las credenciales de tu base de datos

r = redis.Redis(
    host='redis-19322.c240.us-east-1-3.ec2.redns.redis-cloud.com',
    port=19322,
    password='sNdNuQ6jLgIHGEF35hn0PaA16AiJMPJd')

canal = 'canal_ejemplo'
pubsub = r.pubsub()

# Suscribirse al canal
pubsub.subscribe(canal)

print(f"Suscrito al canal: {canal}")
# Escuchar los mensajes en tiempo real
for mensaje in pubsub.listen():
    if mensaje['type'] == 'message':
        print(f"Recibido: {mensaje['data'].decode('utf-8')}")
