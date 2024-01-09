from fastapi import FastAPI
from cat_wrapper import CATWrapper

app = FastAPI(title = 'Wrapper Cataluña', version = '0.0.1', description = 'API de búsqueda para la comunidad de Cataluña')

@app.get('/', name = 'Get cataluña data')
def getJSON():
    wrapper = CATWrapper()
    return wrapper.getJSON()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8082)