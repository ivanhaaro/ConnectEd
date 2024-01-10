import React from 'react';
import './Tabla.css';
const DatosTabla = ({ centrosEducativos }) => {
  // Verificar si hay datos
  if (!centrosEducativos || centrosEducativos.length === 0) {
    return <p>No hay datos disponibles.</p>;
  }

  // Excluir la columna "id"
  const columnas = Object.keys(centrosEducativos[0]).filter(
    (columna) => columna !== 'id' && columna !== 'latitud' && columna !== 'longitud'
  );
  

  return (
    <table>
      <thead>
        <tr>
          {columnas.map((columna) => (
            <th key={columna}>{columna}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {centrosEducativos.map((fila, index) => (
          <tr key={index}>
            {columnas.map((columna) => (
              <td key={columna}>{fila[columna]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default DatosTabla;
