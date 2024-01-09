import React from "react";
import SearchForm from "./SearchForm";
import MapDisplay from "./MapDisplay";
import "./App.css";
import Navbar from "./NavBar";
import { fetchCentrosEducativos } from "./api"; 
import Carga from "./Carga";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  const [centrosEducativos, setCentrosEducativos] = React.useState([]);

  const handleSearchSubmit = async (data) => {
    try {
      const centrosEducativosTemp = await fetchCentrosEducativos(data);
      setCentrosEducativos(centrosEducativosTemp);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

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
            />
          }
        />
        <Route path="/carga" element={<Carga />} />
      </Routes>
    </Router>
  );
}
const HomeSearchForm = ({ onSubmit, centrosEducativos }) => (
  <>
    <SearchForm onSubmit={onSubmit} />
    <MapDisplay centrosEducativos={centrosEducativos} />
  </>
);

export default App;
