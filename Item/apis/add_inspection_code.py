from Item.models import InspectionCode

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE


def add_inspection_code(request):
    """ 新增检验代码
    POST请求
    """
    name = request.json.get('name')

    InspectionCode.objects.create(
        name=name,
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
