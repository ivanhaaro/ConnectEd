from fastapi import FastAPI
from cv_wrapper import CVWrapper

app = FastAPI(title = 'Wrapper Comunidad Valenciana', version = '0.0.1', description = 'API de búsqueda para la Comunidad Valenciana')

@app.get('/', name = 'Get comunidad valenciana data')
def getJSON():
    wrapper = CVWrapper()
    return wrapper.getJSON()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8083)