from fastapi import FastAPI, APIRouter, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

import user.routers as user_routers
import events.routers as events_routers
import marketplace.routers as marketplace_routers
import uvicorn

prefix_router = APIRouter(
    prefix='/api',
)

prefix_router.include_router(user_routers.router)
prefix_router.include_router(events_routers.router)
prefix_router.include_router(marketplace_routers.router)

app = FastAPI(title='Hackaton Finodays API', docs_url='/')
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

app.include_router(prefix_router)

#app.mount('/', StaticFiles(directory='./dist', html=True))

if __name__ == '__main__':
    uvicorn.run('__main__:app', host='127.0.0.1', port=8000, reload=True)
