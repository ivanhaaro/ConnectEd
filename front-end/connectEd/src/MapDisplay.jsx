import React, { useState, useMemo } from 'react';
import {GoogleMap, useLoadScript, MarkerF, InfoWindow, Marker, LoadScript} from '@react-google-maps/api';
// import Box from '@mui/material/Box';
import './MapDisplay.css';

const markers = [
  {
    id: 1,
    name: 'Nick eres un putero',
    position: { lat: 38.9984922, lng: -0.1654128}

  },
  {
    id: 2,
    name: 'Nick eres un putero y además un ratón',
    position: { lat: 38.20250862278044, lng: -1.0461902618408203}
  } 
]

const MapDisplay = ({ centrosEducativos }) => {
  // const { isLoaded } = useLoadScript({
  //   googleMapsApiKey: 'AIzaSyDI0bLLisjbLkXAjUD52_g_sZKGqGGn1jQ'
  // })

  const mapStyles = {
    height: '50%',
    width: '100%',
  };

  const handleMarkerClick = (marker) => {
    setActivePosition(marker.position);
    // if(marker === activeMarker) {
    //   return;
    // }
    setSelectedMarker(marker);
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
        >
          <div>
            <h3>Información del Marcador</h3>
            <p>{selectedMarker.name}</p>
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

        {renderInfoWindow()}
      </GoogleMap>
  ));

  return (
    <LoadScript googleMapsApiKey="AIzaSyDI0bLLisjbLkXAjUD52_g_sZKGqGGn1jQ">
      {memoizedMap}
    </LoadScript>
  );
};

export default MapDisplay;
