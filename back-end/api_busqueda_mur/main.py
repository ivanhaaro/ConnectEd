from fastapi import FastAPI
from mur_wrapper import MURWrapper

app = FastAPI(title = 'Wrapper Murcia', version = '0.0.1', description = 'API de búsqueda para la comunidad de Murcia')

@app.get('/', name = 'Get murcia data')
def getJSON():
    wrapper = MURWrapper()
    return wrapper.getJSON()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8081)