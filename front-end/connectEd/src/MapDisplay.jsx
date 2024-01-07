import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import './MapDisplay.css';
import Box from '@mui/material/Box';


const MapDisplay = ({ centrosEducativos }) => {
  const position = [38.9984922, -0.1654128]; // Default position, change to your needs

  return (
    <Box sx={{ height: 730, width: '100%', marginTop: 2 }}>
      <MapContainer center={position} zoom={13} style={{ height: '100%', width: '100%' }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors'
        />
        // Tus marcadores y popups
      </MapContainer>
      {centrosEducativos.map(centro => (
        <Marker key={centro.id} position={[centro.latitud, centro.longitud]}>
          <Popup>
            {centro.nombre} - {centro.informacionAdicional}
          </Popup>
        </Marker>
      ))}
    </Box>
  );
};

export default MapDisplay;
