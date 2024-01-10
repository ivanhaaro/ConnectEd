import React, { useEffect, useState } from "react";
import SearchForm from "./SearchForm";
import MapDisplay from "./MapDisplay";
import "./App.css";
import Navbar from "./NavBar";
import { fetchCentrosEducativos, fetchCentrosEducativosAll } from "./api"; 
import Carga from "./Carga";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import DatosTabla from "./Tabla";

function App() {
  const [centrosEducativos, setCentrosEducativos] = React.useState([]);
  const [centrosEducativosTodos, setCentrosEducativosAll] = React.useState([]);
  const [cargando, setCargando] = useState(true); // Estado para manejar la carga

  useEffect(() => {
    const cargarDatos = async () => {
      try {
        const centrosEducativosAllTemp = await fetchCentrosEducativosAll();
        setCentrosEducativosAll(centrosEducativosAllTemp);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setCargando(false); // Finaliza la carga independientemente de si hubo un error
      }
    };
    cargarDatos();
  }, []);

  const handleSearchSubmit = async (data) => {
    try {
      console.log("se hace con data = "+ data);
      const centrosEducativosTemp = await fetchCentrosEducativos(data);
      setCentrosEducativos(centrosEducativosTemp);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  if (cargando) {
    return <div>Cargando datos...</div>; // O algún componente de carga
  }
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route
          path="/"
          element={
            <HomeSearchForm
              onSubmit={handleSearchSubmit}
              centrosEducativos={centrosEducativos}
              centrosEducativosTodos= {centrosEducativosTodos}
            />
          }
        />
        <Route path="/carga" element={<Carga />} />
      </Routes>
    </Router>
  );
}
const HomeSearchForm = ({ onSubmit, centrosEducativos, centrosEducativosTodos }) => (
  <>
    <SearchForm onSubmit={onSubmit} />
    <MapDisplay centrosEducativos={centrosEducativosTodos} />
    <div className="tableDatos">
      <div className="table-container">
      <DatosTabla centrosEducativos={centrosEducativos} />
      </div>
    </div>
    
  </>
);

export default App;
