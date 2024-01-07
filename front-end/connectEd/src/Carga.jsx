import React, { useState, useEffect } from "react";
import "./Carga.css";

// Simulación de datos de la base de datos
const datosDeLaBD = {
  Valencia: "Información de la Comunidad Valenciana",
  Murcia: "Información de Murcia",
  Cataluña: "Información de Cataluña",
};

const App = () => {
  // Estado para el título
  const [titulo, setTitulo] = useState("Carga del almacén de datos");

  // Estado para las fuentes seleccionadas
  const [fuentesSeleccionadas, setFuentesSeleccionadas] = useState([]);

  // Estado para el texto de información
  const [textoInformacion, setTextoInformacion] = useState("");

  // Función para cargar la información de la base de datos
  const cargarInformacion = () => {
    // Simulación de carga de datos desde la base de datos
    const informacion = fuentesSeleccionadas
      .map((fuente) => datosDeLaBD[fuente])
      .join("\n");

    setTextoInformacion(informacion);
  };

  // Efecto para cargar la información cuando cambian las fuentes seleccionadas
  useEffect(() => {
    cargarInformacion();
  }, [fuentesSeleccionadas]);

  // Función para manejar el cambio en las fuentes seleccionadas
  const handleCheckboxChange = (fuente) => {
    const nuevasFuentesSeleccionadas = fuentesSeleccionadas.includes(fuente)
      ? fuentesSeleccionadas.filter((f) => f !== fuente)
      : [...fuentesSeleccionadas, fuente];

    setFuentesSeleccionadas(nuevasFuentesSeleccionadas);
  };

  // Función para manejar la selección/deselección de todas las fuentes
  const handleSelectAll = () => {
    if (fuentesSeleccionadas.length === Object.keys(datosDeLaBD).length) {
      // Deseleccionar todas si todas están seleccionadas
      setFuentesSeleccionadas([]);
    } else {
      // Seleccionar todas si no todas están seleccionadas
      setFuentesSeleccionadas(Object.keys(datosDeLaBD));
    }
  };

  return (
    <div>
      {/* Título */}
      <h1>{titulo}</h1>

      <h2>Selección de Datos</h2>

      {/* Selector de fuentes */}
      <div class="contenedor-izquierda">
        <label>
          <input
            type="checkbox"
            checked={
              fuentesSeleccionadas.length === Object.keys(datosDeLaBD).length
            }
            onChange={handleSelectAll}
          />
          Seleccionar todas
        </label>
        {Object.keys(datosDeLaBD).map((fuente) => (
          <div key={fuente}>
            <label>
              <input
                type="checkbox"
                checked={fuentesSeleccionadas.includes(fuente)}
                onChange={() => handleCheckboxChange(fuente)}
              />
              {fuente}
            </label>
          </div>
        ))}
      </div>

      {/* Cuadro de texto con información */}
      <div>
        <textarea rows="10" cols="50" value={textoInformacion} readOnly />
      </div>
    </div>
  );
};

export default App;
