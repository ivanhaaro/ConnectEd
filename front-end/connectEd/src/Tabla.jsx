import React from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
import "./Tabla.css";

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
    <TableContainer component={Paper} sx={{ maxHeight: 400, margin: 0, padding: 0 }}>
      <Table stickyHeader aria-label="sticky table">
        <TableHead>
          <TableRow>
            {columnas.map((columna) => (
              <TableCell 
                key={columna}
                style={{ backgroundColor: '#1976d2', color: '#fff', fontWeight: 'bold' }}
              >
                {columna.charAt(0).toUpperCase() + columna.slice(1)}
              </TableCell>
            ))}
          </TableRow>
        </TableHead>
        <TableBody>
          {centrosEducativos.map((fila, index) => (
            <TableRow key={index}>
              {columnas.map((columna) => (
                <TableCell key={columna}>{fila[columna]}</TableCell>
              ))}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default DatosTabla;
