from classy_fastapi import Routable, get

from ..models import HealthCheck


class HealthCheckRoutes(Routable):
    @get(
        "/health-check/",
        operation_id="health_check",
        summary="Health check",
        response_model=HealthCheck,
    )
    async def get_data_products(self) -> dict:
        """Returns a 200 status code if the service is up and running"""
        return {"status": "OK"}


routes = HealthCheckRoutes()
