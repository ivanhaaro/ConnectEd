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
  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const data = Object.fromEntries(formData.entries());
    onSubmit(data);
  };
  const [tipoCentro, setTipoCentro] = React.useState("");

  const handleChange = (event) => {
    setTipoCentro(event.target.value);
  };

  return (
    <form onSubmit={handleSubmit}>
      <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
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
          type="submit"
          fullWidth
          variant="contained"
          sx={{ mt: 3, mb: 2 }}
        >
          Buscar
        </Button>
      </Box>
    </form>
  );
};

export default SearchForm;
