import React from 'react';
import SearchForm from './SearchForm';
import MapDisplay from './MapDisplay';
import './App.css';
import Navbar from './NavBar';
import Container from '@mui/material/Container';

function App() {
  const [centrosEducativos, setCentrosEducativos] = React.useState([]);

  const handleSearchSubmit = async (data) => {
    const response = await fetch('connectEd/busqueda', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const centrosEducativosTemp = await response.json();
    setCentrosEducativos(centrosEducativosTemp);
  };


  return (
    <Container maxWidth="false">
      <Navbar />
      <SearchForm onSubmit={handleSearchSubmit}/>
      <MapDisplay centrosEducativos={centrosEducativos}/>
    </Container>
  );
}

export default App;
