import React, { useState, useMemo } from 'react';
import {GoogleMap, useLoadScript, MarkerF, InfoWindow, Marker, LoadScript} from '@react-google-maps/api';
// import Box from '@mui/material/Box';
import './MapDisplay.css';




const MapDisplay = ({ centrosEducativos }) => {
  // const { isLoaded } = useLoadScript({
  //   googleMapsApiKey: 'AIzaSyDI0bLLisjbLkXAjUD52_g_sZKGqGGn1jQ'
  // })

  const markers = centrosEducativos.map((centro, index) => ({
    id: index,
    name: centro.nombre,
    position: {
      lat: centro.latitud,
      lng: centro.longitud,
    },
  }));

  const [isInfoWindowOpen, setIsInfoWindowOpen] = useState(false);

  const mapStyles = {
    height: '50%',
    width: '100%',
  };

  const handleMarkerClick = (marker) => {
    setActivePosition(marker.position);
    if(marker === selectedMarker) {
      return;
    }
    setSelectedMarker(marker);
    setIsInfoWindowOpen(true);
  };

  const handleInfoWindowClose = () => {
    setIsInfoWindowOpen(false);
    setSelectedMarker(null);
  };

  const mapOptions = {
    styles: [
      {
        featureType: 'poi',
        elementType: 'labels',
        stylers: [
          { visibility: 'off' }, // Oculta los puntos de interés (marcadores predeterminados)
        ],
      },
    ],
  };

  const [position, setActivePosition] = React.useState({ lat: 38.9984922, lng: -0.1654128 });

  const [selectedMarker, setSelectedMarker] = React.useState(null);

  const renderInfoWindow = () => {
    if (selectedMarker && selectedMarker.name) {
      return (
        <InfoWindow
          position={selectedMarker.position}
          onCloseClick={() => setSelectedMarker(null)}
          style={{ background: 'white', color: 'black' }}
        >
          <div>
            <h3>Información del Marcador</h3>
            <p>{selectedMarker.name}</p>
            <p> </p>
            <p> </p>
            <p> </p>
          </div>
        </InfoWindow>
      );
    }
    return null;
  };

  const memoizedMap = useMemo (
    () => (
      <GoogleMap mapContainerStyle={mapStyles} options={mapOptions} center={position} zoom={13}>
        {markers.map((marker) => (
          <MarkerF
            key={marker.id}
            position={marker.position}
            onClick={() => handleMarkerClick(marker)}
          />
        ))}

        {selectedMarker && (
          <InfoWindow
            position={selectedMarker.position}
            onCloseClick={handleInfoWindowClose}
          >
            <div className='marcador'>
              <h3>Información del Marcador</h3>
              <p>{selectedMarker.name}</p>
              <p>.</p>
            </div>
          </InfoWindow>
        )}
      </GoogleMap>
  ));

  return (
    <LoadScript googleMapsApiKey="AIzaSyDI0bLLisjbLkXAjUD52_g_sZKGqGGn1jQ">
      {memoizedMap}
    </LoadScript>
  );
};

export default MapDisplay;
