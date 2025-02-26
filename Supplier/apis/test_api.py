from django.http import JsonResponse


def test_api(request):
    """ 测试api
    GET请求
    """
    return JsonResponse(data={
        "res": 'success',
    })
