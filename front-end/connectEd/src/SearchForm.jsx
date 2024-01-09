import React from "react";
import "./SearchForm.css";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";
import InputLabel from "@mui/material/InputLabel";
import FormControl from "@mui/material/FormControl";

const SearchForm = ({ onSubmit }) => {
  const handleClick = () => {
    const formData = {
      localidad: document.getElementById("locality").value,
      codigo_postal: document.getElementById("postalcode").value,
      provincia: document.getElementById("province").value,
      tipo: tipoCentro,
    };

    onSubmit(formData);
  };

  const [tipoCentro, setTipoCentro] = React.useState("");

  const handleChange = (event) => {
    setTipoCentro(event.target.value);
  };

  return (
    <Box component="div" noValidate sx={{ mt: 1 }}>
      <Grid container spacing={2}>
        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            margin="normal"
            required
            id="locality"
            label="Localidad"
            name="locality"
            autoFocus
          />
        </Grid>
        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            margin="normal"
            id="postalcode"
            label="Código Postal"
            name="CodigoPostal"
          />
        </Grid>
        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            margin="normal"
            id="province"
            label="Provincia"
            name="Provincia"
          />
        </Grid>
        <Grid item xs={12} md={6}>
          <FormControl fullWidth margin="normal">
            <InputLabel id="tipo-centro-label">Tipo de Centro</InputLabel>
            <Select
              labelId="tipo-centro-label"
              id="tipo-centro"
              value={tipoCentro}
              label="Tipo de Centro"
              onChange={handleChange}
            >
              <MenuItem value={"Privado"}>Privado</MenuItem>
              <MenuItem value={"Concertado"}>Concertado</MenuItem>
              <MenuItem value={"Publico"}>Público</MenuItem>
              <MenuItem value={"Otros"}>Otros</MenuItem>
            </Select>
          </FormControl>
        </Grid>
      </Grid>
      <Button
        type="button"
        onClick={handleClick}
        fullWidth
        variant="contained"
        sx={{ mt: 3, mb: 2 }}
      >
        Buscar
      </Button>
    </Box>
  );
};

export default SearchForm;
