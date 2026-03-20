# Estándares de Registro de Logs de CONFIANZA23 (Loguru)

## Contexto
Registro de logs estandarizado para todas las aplicaciones de Python en CONFIANZA23.

## Implementación
```python
from loguru import logger

# Configuración recomendada
logger.add("logs/app_{time}.log", rotation="10 MB", retention="10 days", level="DEBUG")

def procesar():
    logger.info("Iniciando proceso...")
    try:
        # lógica de negocio
        logger.debug("Estado intermedio: {estado}", estado=datos)
    except Exception as e:
        logger.exception("Fallo al procesar") 
```

## Reglas
- **NUNCA** usar `print()` simple para la depuración en aplicaciones listas para producción.
- **SIEMPRE** registrar fallos críticos con `logger.error` o `logger.exception`.
- **USAR** `logger.success` para la finalización exitosa de tareas importantes.
