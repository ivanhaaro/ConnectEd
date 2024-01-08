// Petición para los centros educativos
export const fetchCentrosEducativos= async (data) => {
    try {
        // Construir la URL con los parámetros
        const queryParams = new URLSearchParams(data).toString();
        const url = `http://127.0.0.1:8000/getEducativeCenters?${queryParams}`;
        
        const response = await fetch(url, {
            method: "GET",
            headers: {
            "Content-Type": "application/json",
            },
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

// Petición para la carga de datos 
export const fetchCargaDatos = async (comunidad) => { 
    try {

        const response = await fetch(`http://127.0.0.1:8000/loadDataBaseData?comunidad=${comunidad}`, {
          method: "GET",
          mode: 'no-cors'
        });
        console.log(response.body);
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
    
        return await response.json();
      } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
      }
}