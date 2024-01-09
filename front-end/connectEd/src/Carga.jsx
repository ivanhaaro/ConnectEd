import React, { useState, useEffect } from "react";
import Button from "@mui/material/Button";
import "./Carga.css";
import { CargaDatosALL, CargaDatosCAT, CargaDatosCV, CargaDatosMUR} from "./api"; 

const Comunidades = {
  Comunidad_Valenciana: "Comunidad_Valenciana",
  Murcia: "Murcia",
  Cataluña: "Cataluña",
};

const Carga = () => {
  // Estado para el título
  const [titulo, setTitulo] = useState("Carga del almacén de datos");

  // Estado para las fuentes seleccionadas
  const [fuentesSeleccionadas, setFuentesSeleccionadas] = useState([]);

  // Estado para el texto de información
  const [textoInformacion, setTextoInformacion] = useState("");

  // Función para cargar la información de la base de datos
  const cargarInformacion = async () => {
  try {
    var response = '';
    const responses = [];
    if (fuentesSeleccionadas.length > 2) {
      const responseAll = await CargaDatosALL();
      var { message, defectos } = await responseAll.json()
      responses.push(message);
      var defectosString = defectos.join('\n');
      responses.push(defectosString);
    } else {
      console.log(fuentesSeleccionadas);
      

      for (const fuente of fuentesSeleccionadas) {
        switch (fuente) {
          case 'Comunidad_Valenciana':
            const responseCv = await CargaDatosCV();
            var { message, defectos } = await responseCv.json();
            responses.push(message);
            var defectosString = defectos.join('\n');
            responses.push(defectosString);
            break;
          case 'Murcia':
            const responseMur = await CargaDatosMUR();
            var { message, defectos } = await responseMur.json();
            responses.push(message);
            var defectosString = defectos.join('\n');
            responses.push(defectosString);
            break;
          case 'Cataluña':
            const responseCat = await CargaDatosCAT();
            var { message, defectos } = await responseCat.json();
            responses.push(message);
            var defectosString = defectos.join('\n');
            responses.push(defectosString);
            break;
          // Agrega más casos según sea necesario para otras fuentes
          default:
            // Acciones predeterminadas si la fuente no coincide con ningún caso
            break;
        }
      }
    }
      response = responses.join('\n');
      // Actualiza el estado del texto de información con el mensaje y los defectos
      setTextoInformacion(response);
    } catch (error) {
      // Manejar el error según tus necesidades
      console.error('Error en cargarInformacion:', error);
      setTextoInformacion(`Error al cargar la información: ${error.message}`);
    }
  };

  // Función para cancelar la carga(borrar formulario)
  const cancelar = () => {
    setFuentesSeleccionadas([]);

    setTextoInformacion("");
  };


  // Función para manejar el cambio en las fuentes seleccionadas
  const handleCheckboxChange = (fuente) => {
    const nuevasFuentesSeleccionadas = fuentesSeleccionadas.includes(fuente)
      ? fuentesSeleccionadas.filter((f) => f !== fuente)
      : [...fuentesSeleccionadas, fuente];

    setFuentesSeleccionadas(nuevasFuentesSeleccionadas);
  };

  // Función para manejar la selección/deselección de todas las fuentes
  const handleSelectAll = () => {
    if (fuentesSeleccionadas.length === Object.keys(Comunidades).length) {
      // Deseleccionar todas si todas están seleccionadas
      setFuentesSeleccionadas([]);
    } else {
      // Seleccionar todas si no todas están seleccionadas
      setFuentesSeleccionadas(Object.keys(Comunidades));
    }
  };

  return (
    <div>
      {/* Título */}
      <h1>{titulo}</h1>

      <h2>Selección de Datos:</h2>

      {/* Selector de fuentes */}
      <div className="cuadricula">
        <div class="contenedor-izquierda">
          <label>
            <input
              type="checkbox"
              checked={
                fuentesSeleccionadas.length === Object.keys(Comunidades).length
              }
              onChange={handleSelectAll}
            />
            Seleccionar todas
          </label>
        </div>
        {Object.keys(Comunidades).map((fuente) => (
          <div key={fuente} class="contenedor-izquierda">
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
      <div className="fila">
        <Button
          type="submit"
          fullWidth
          variant="contained"
          sx={{ mt: 3, mb: 2 }}ç
          onClick={cancelar}
        >
          Cancelar
        </Button>

        <Button
          type="submit"
          fullWidth
          variant="contained"
          sx={{ mt: 3, mb: 2 }}
          onClick={cargarInformacion}
        >
          Cargar
        </Button>
      </div>

      <h2>Resultados de la Carga:</h2>

      {/* Cuadro de texto con información */}
      <div>
        <textarea rows="10" cols="50" value={textoInformacion} readOnly />
      </div>
    </div>
  );
};

export default Carga;
