from drf_yasg import openapi
from drf_yasg.openapi import Schema
from rest_framework import status


class StartechPriceApiSchemaView:
    tags = ['Startech Search API']
    request_schema = Schema(
        title="Request Data Example",
        type=openapi.TYPE_OBJECT,
        properties={
            "product_name": Schema(type=openapi.TYPE_STRING, default=""),
        },
    )
    responses = {
        status.HTTP_200_OK: openapi.Response(
            description="Startech Product Search List",
            schema=Schema(
                title="Success Response Example",
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": Schema(type=openapi.TYPE_BOOLEAN, default="False"),
                    "message": Schema(
                        type=openapi.TYPE_STRING,
                        default="Startech product search list returned successfully",
                    ),
                    "data": Schema(type=openapi.TYPE_OBJECT),
                },
            ),
        ),
        status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
            description="Unsuccessful/Error Example",
            schema=Schema(
                title="",
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": Schema(type=openapi.TYPE_BOOLEAN, default="True"),
                    "message": Schema(
                        type=openapi.TYPE_STRING,
                        default="Could not retrieve startech product search list",
                    ),
                    "data": Schema(type=openapi.TYPE_OBJECT, default=None),
                },
            ),
        ),
    }
