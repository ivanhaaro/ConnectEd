import React from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";

const NavBar = () => {
  return (
    <AppBar position="static" style={{ width: "100%" }}>
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          ConnectEd
        </Typography>
        <Button color="inherit">Inicio</Button>
        <Button color="inherit">Carga de Datos</Button>
      </Toolbar>
    </AppBar>
  );
};

export default NavBar;
