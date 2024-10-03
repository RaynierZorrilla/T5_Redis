import redis
import time

# Conexión a Redis con las credenciales de tu base de datos
r = redis.Redis(
    host='redis-19322.c240.us-east-1-3.ec2.redns.redis-cloud.com',
    port=19322,
    password='sNdNuQ6jLgIHGEF35hn0PaA16AiJMPJd')

canal = 'canal_ejemplo'

# Publicar mensajes en el canal
for i in range(5):
    mensaje = f"Mensaje {i+1}"
    r.publish(canal, mensaje)
    print(f"Publicado: {mensaje}")
    time.sleep(1)  # Pausa entre publicaciones
