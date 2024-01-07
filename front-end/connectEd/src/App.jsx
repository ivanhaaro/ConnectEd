import React from "react";
import SearchForm from "./SearchForm";
import MapDisplay from "./MapDisplay";
import "./App.css";
import Navbar from "./NavBar";
import Container from "@mui/material/Container";
import Carga from "./Carga";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  const [centrosEducativos, setCentrosEducativos] = React.useState([]);

  const handleSearchSubmit = async (data) => {
    const response = await fetch("connectEd/busqueda", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const centrosEducativosTemp = await response.json();
    setCentrosEducativos(centrosEducativosTemp);
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
