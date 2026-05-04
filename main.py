from fastapi import FastAPI
from routes import  upload_routes, weather_routes, analysis, visualisation

app = FastAPI()


app.include_router(upload_routes.router, prefix="/api", tags=["Upload"])
app.include_router(weather_routes.router, prefix="/api", tags=["Weather CRUD"])
app.include_router(analysis.router, prefix="/api", tags=["Analysis"])
app.include_router(visualisation.router, prefix="/api", tags=["Visualization"])

@app.get("/")
def root():
    return {"message": "Weather Analytics API is running "}