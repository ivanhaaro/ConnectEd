import React from 'react';
import GoogleMapReact from 'google-map-react';
// import Box from '@mui/material/Box';
import './MapDisplay.css';

const AnyReactComponent = ({ text }) => <div>{text}</div>;

const MapDisplay = ({ centrosEducativos }) => {
  const position = { lat: 38.9984922, lng: -0.1654128 }; // Default position

  return (
    <div style={{ height: '50%', width: '100%' }}>
      <GoogleMapReact
        bootstrapURLKeys={{ key: 'AIzaSyDI0bLLisjbLkXAjUD52_g_sZKGqGGn1jQ' }}
        defaultCenter={position}
        defaultZoom={13}
        yesIWantToUseGoogleMapApiInternals
      >
        {centrosEducativos.map(centro => (
          <AnyReactComponent
            key={centro.nombre}
            lat={centro.latitud}
            lng={centro.longitud}
            text={centro.nombre}
          />
        ))}
      </GoogleMapReact>
    </div>
  );
};

export default MapDisplay;
