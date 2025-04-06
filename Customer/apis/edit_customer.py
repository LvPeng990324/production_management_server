from Customer.models import Customer

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.permission_check import login_required


@login_required
def edit_customer(request):
    """ 编辑客户
    POST请求
    """
    customer_id = request.json.get('customer_id')
    name = request.json.get('name')
    contact_person = request.json.get('contact_person')
    phone = request.json.get('phone')
    email = request.json.get('email')
    tax_number = request.json.get('tax_number')
    address = request.json.get('address')
    bank_card_number = request.json.get('bank_card_number')
    bank_name = request.json.get('bank_name')

    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "message": '该客户不存在',
        })

    # 记录本次修改的内容描述
    edit_log_str = ''

    # 修改
    if name != customer.name:
        edit_log_str += f'名字：{customer.name} -> {name}\n'
        customer.name = name

    if contact_person != customer.contact_person:
        edit_log_str += f'联系人：{customer.contact_person} -> {contact_person}\n'
        customer.contact_person = contact_person

    if phone != customer.phone:
        edit_log_str += f'手机号：{customer.phone} -> {phone}\n'
        customer.phone = phone

    if email != customer.email:
        edit_log_str += f'邮箱：{customer.email} -> {email}\n'
        customer.email = email

    if tax_number != customer.tax_number:
        edit_log_str += f'税号：{customer.tax_number} -> {tax_number}\n'
        customer.tax_number = tax_number

    if address != customer.address:
        edit_log_str += f'地址：{customer.address} -> {address}\n'
        customer.address = address

    if bank_card_number != customer.bank_card_number:
        edit_log_str += f'银行卡号：{customer.bank_card_number} -> {bank_card_number}\n'
        customer.bank_card_number = bank_card_number

    if bank_name != customer.bank_name:
        edit_log_str += f'开户行：{customer.bank_name} -> {bank_name}\n'
        customer.bank_name = bank_name

    customer.save()

    # 记录用户日志
    add_user_log(
        request=request,
        action='编辑客户',
        detail=edit_log_str,
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
