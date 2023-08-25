import logging as log

# docs.phyton.org/3/howto/loggin.html
# Llamamos una configuración básica

log.basicConfig(level=log.INFO,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s]%(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.basicConfig(level=log.DEBUG)
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critical')
 