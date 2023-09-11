package utn.estudiantes.servicio;

import utn.estudiantes.modelo.Estudiantes;

import java.util.List;

public interface IEstudianteServicio {
    public List<Estudiantes> listarEstudiantes();
    public Estudiantes buscarEstudiantePorId(Integer idEstudiante);
    public void guardarEstudiante(Estudiantes estudiante);
    public void eliminarEstudiante(Estudiantes estudiante);
}
