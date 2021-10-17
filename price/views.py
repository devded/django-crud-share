from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from price.schema import StartechPriceApiSchemaView
from price.services.startech import StartechPriceService


class StartechPriceApiView(APIView):
    @swagger_auto_schema(
        tags=StartechPriceApiSchemaView.tags,
        request_body=StartechPriceApiSchemaView.request_schema,
        responses=StartechPriceApiSchemaView.responses,
    )
    def post(self, request):
        product_name = request.data.get('product_name')
        startech_price = StartechPriceService.get_price(product_name)
        return Response(startech_price)
