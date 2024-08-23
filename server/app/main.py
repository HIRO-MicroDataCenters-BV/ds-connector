from typing import Any, Dict

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from prometheus_fastapi_instrumentator import Instrumentator

from .config import CONNECTORS
from .core import init_repository
from .rest_api.routes import data_products, health_check

init_repository(CONNECTORS)


class CustomFastAPI(FastAPI):
    def openapi(self) -> Dict[str, Any]:
        if self.openapi_schema:
            return self.openapi_schema
        openapi_schema = get_openapi(
            title="Data Space Connector service",
            version="0.1.0",
            description="This connector requests data from the data layer and "
            "provides a REST API for servicing requests from the catalog "
            "service.",
            contact={
                "name": "HIRO-MicroDataCenters",
                "email": "all-hiro@hiro-microdatacenters.nl",
            },
            license_info={
                "name": "MIT",
                "url": "https://github.com/HIRO-MicroDataCenters-BV"
                "/ds-connector/blob/main/LICENSE",
            },
            routes=self.routes,
        )
        self.openapi_schema = openapi_schema
        return self.openapi_schema


app = CustomFastAPI()
Instrumentator().instrument(app).expose(app)

app.include_router(health_check.routes.router)
app.include_router(data_products.routes.router)
