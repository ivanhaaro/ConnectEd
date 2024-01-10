// Petición para los centros educativos
export const fetchCentrosEducativos= async (data) => {
    try {
        // Construir la URL con los parámetros
        const filteredData = Object.fromEntries(
          Object.entries(data).filter(([_, value]) => value !== "")
        );
        const queryParams = new URLSearchParams(filteredData).toString();
        const url = `http://127.0.0.1:8001/getEducativeCenters?${queryParams}`;
        console.log(url);
        const response = await fetch(url, {
            method: "GET",
        });
        
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return await response.json();
    } catch (error) {
      console.error('Error fetching data:', error);
      throw error; 
    }
  };

export const fetchCentrosEducativosAll= async () => {
  try {
      const url = `http://127.0.0.1:8001/getEducativeCenters?`;
      console.log(url);
      const response = await fetch(url, {
          method: "GET",
      });
      
      if (!response.ok) {
          throw new Error("Network response was not ok");
      }
      return await response.json();
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error; 
  }
};  

// Petición para la carga de datos de Murcia
export const CargaDatosMUR = async () => { 
    try {

        const response = await fetch(`http://127.0.0.1:8000/loadDataMUR`, {
          method: "GET",
        });
        
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }

        return await response;
      } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
      }
}

// Petición para la carga de datos de la Comunidad Valenciana
export const CargaDatosCV = async () => { 
  try {

      const response = await fetch(`http://127.0.0.1:8000/loadDataCV`, {
        method: "GET"
      });
      console.log(response.body);
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
  
      return await response;
    } catch (error) {
      console.error('Error fetching data:', error);
      throw error;
    }
}
// Petición para la carga de datos de Cataluña
export const CargaDatosCAT = async () => { 
  try {

      const response = await fetch(`http://127.0.0.1:8000/loadDataCAT`, {
        method: "GET"
      });
      console.log(response.body);
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
  
      return await response;
    } catch (error) {
      console.error('Error fetching data:', error);
      throw error;
    }
}

// Petición para la carga de datos de todas las comunidades
export const CargaDatosALL= async () => { 
  try {

      const response = await fetch(`http://127.0.0.1:8000/loadDataALL`, {
        method: "GET"
      });
      console.log(response.body);
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
  
      return await response;
    } catch (error) {
      console.error('Error fetching data:', error);
      throw error;
    }
}
