from Usuario import Usuario
from cursor_del_pool import CursorDelPool
from logger_base import log

class UsuarioDAO:
    '''
    DAO -> Data Access Object Para la tabla de usuario
    CRUD -> Create - Read - Update - Delete
    '''

    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.username, usuario.password, usuario._id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount

if __name__ == '__main__':
    # Eliminar un usuario
    usuario = Usuario(id_usuario=3)
    usuario_eliminado = UsuarioDAO.eliminar(usuario)
    log.debug(f'Usuarios eliminados: {usuario_eliminado}')

    # Actualizar un registro
    usuario = Usuario(id_usuario=1, username='', password='369')
    usuario_modificado = UsuarioDAO.actualizar(usuario)
    log.debug(f'Usuarios actualizados: {usuario_modificado}')

    # Insertar un usuario
    usuario = Usuario(username='Kely', password='321')
    usuario_insertado = UsuarioDAO.insertar(usuario)
    log.debug(f'Usuario insertado: {usuario_insertado}')

    # Listar o seleccionar
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)