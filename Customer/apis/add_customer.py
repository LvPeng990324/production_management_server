from Customer.models import Customer

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.permission_check import login_required


@login_required
def add_customer(request):
    """ 新增客户
    POST请求
    """
    name = request.json.get('name')
    contact_person = request.json.get('contact_person')
    phone = request.json.get('phone')
    email = request.json.get('email')
    tax_number = request.json.get('tax_number')
    address = request.json.get('address')
    bank_card_number = request.json.get('bank_card_number')
    bank_name = request.json.get('bank_name')

    Customer.objects.create(
        name=name,
        contact_person=contact_person,
        phone=phone,
        email=email,
        tax_number=tax_number,
        address=address,
        bank_card_number=bank_card_number,
        bank_name=bank_name,
    )

    # 记录用户日志
    add_user_log(
        request=request,
        action='新增客户',
        detail=f'''名字：{name}
        联系人：{contact_person}
        手机号：{phone}
        邮箱：{email}
        税号：{tax_number}
        地址：{address}
        银行卡号：{bank_card_number}
        开户行：{bank_name}
''',
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        'res': 'success',
    })
