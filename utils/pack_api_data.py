from Order.models import Order
from Supplier.models import Supplier
from Item.models import Item
from Item.models import TechnicalChange
from Item.models import InspectionCode
from SystemManagement.models import UserLog

from utils.data_covert import datetime_to_str
from utils.data_covert import fen_to_yuan
from utils.data_calc import calc_item_total_cost
from utils.data_calc import calc_order_total_cost
from utils.data_calc import calc_item_level
from utils.data_calc import calc_item_total_num


def pack_order_info(order: Order):
    """ 打包订单信息
    """
    return {
        "order_id": order.id,
        "order_num": order.order_num,
        "order_status": order.order_status,
        "order_start_time": str(order.order_start_time),
        "total_cost": fen_to_yuan(calc_order_total_cost(order=order)),
    }


def pack_order_info_list(orders: list[Order]):
    """ 打包订单信息列表
    """
    order_info_list = []
    for order in orders:
        order_info_list.append(pack_order_info(order=order))
    
    return order_info_list


def pack_order_select_info_list(orders: list[Order]):
    """ 打包订单选项信息列表
    """
    order_select_info_list = []
    for order in orders:
        order_select_info_list.append({
            "value": order.id,
            "label": order.order_num,
        })
    
    return order_select_info_list


def pack_supplier_info(supplier: Supplier):
    """ 打包供应商信息
    """
    return {
        "supplier_id": supplier.id,
        "name": supplier.name,
        "phone": supplier.phone,
    }


def pack_supplier_info_list(suppliers: list[Supplier]):
    """ 打包供应商信息列表
    """
    supplier_info_list = []
    for supplier in suppliers:
        supplier_info_list.append(pack_supplier_info(supplier=supplier))
    
    return supplier_info_list


def pack_item_info(item: Item):
    """ 打包物品信息
    """
    # 打包订单号
    order_num = '/'
    if item.order:
        order_num = item.order.order_num

    # 打包上级物品名称
    parent_item_name = '/'
    if item.parent_item:
        parent_item_name = item.parent_item.name
    
    # 打包技术变更数量
    technical_change_count = item.technicalchange_set.count()

    # 打包检验代码
    inspection_code_id_list = []
    inspection_code_name_list = []
    inspection_codes = item.inspection_codes.all()
    for inspection_code in inspection_codes:
        inspection_code_id_list.append(inspection_code.id)
        inspection_code_name_list.append(inspection_code.name)

    return {
        "item_id": item.id,
        "name": item.name,
        "order_num": order_num,
        "order_id": item.order_id,
        "parent_item_name": parent_item_name,
        "parent_item_id": item.parent_item_id,
        "technical_change_count": technical_change_count,
        "inspection_code_id_list": inspection_code_id_list,
        "inspection_code_name_list": inspection_code_name_list,
        "cost": fen_to_yuan(item.cost),
        "total_cost": fen_to_yuan(calc_item_total_cost(item=item)),
        "level": calc_item_level(item=item),
        "num": item.num,
        "total_num": calc_item_total_num(item=item),
    }


def pack_item_info_list(items: list[Item]):
    """ 打包物品信息列表
    """
    item_info_list = []
    for item in items:
        item_info_list.append(pack_item_info(item=item))
    
    return item_info_list


def pack_item_select_info_list(items: list[Item]):
    """ 打包物品选项信息列表
    """
    item_select_info_list = []
    for item in items:
        item_select_info_list.append({
            "value": item.id,
            "label": item.name,
        })
    
    return item_select_info_list


def pack_technical_change_info(technical_change: TechnicalChange):
    """ 打包技术变更信息
    """
    # 打包物品名称
    item_name = '/'
    if technical_change.item:
        item_name = technical_change.item.name

    return {
        "technical_change_id": technical_change.id,
        "name": technical_change.name,
        "item_name": item_name,
        "item_id": technical_change.item_id,
    }


def pack_technical_change_info_list(technical_changes: list[TechnicalChange]):
    """ 打包技术变更信息列表
    """
    technical_change_info_list = []
    for technical_change in technical_changes:
        technical_change_info_list.append(pack_technical_change_info(technical_change=technical_change))
    
    return technical_change_info_list


def pack_inspection_code_info(inspection_code: InspectionCode):
    """ 打包检验代码信息
    """
    return {
        "inspection_code_id": inspection_code.id,
        "name": inspection_code.name,
    }


def pack_inspection_code_info_list(inspection_codes: list[InspectionCode]):
    """ 打包检验代码信息列表
    """
    inspection_code_info_list = []
    for inspection_code in inspection_codes:
        inspection_code_info_list.append(pack_inspection_code_info(inspection_code=inspection_code))
    
    return inspection_code_info_list


def pack_inspection_code_select_info_list(inspection_codes: list[InspectionCode]):
    """ 打包检验代码选项信息列表
    """
    inspection_code_select_info_list = []
    for inspection_code in inspection_codes:
        inspection_code_select_info_list.append({
            "value": inspection_code.id,
            "label": inspection_code.name,
        })
    
    return inspection_code_select_info_list


def pack_user_log_info(user_log: UserLog):
    """ 打包用户日志信息
    """
    # 打包用户名称
    user_name = '/'
    if user_log.user:
        user_name = user_log.user.name

    return {
        "user_log_id": user_log.id,
        "user_name": user_name,
        "action": user_log.action,
        "detail": user_log.detail,
        "create_time": datetime_to_str(user_log.create_time),
    }


def pack_user_log_info_list(user_logs: list[UserLog]):
    """ 打包用户日志信息列表
    """
    user_log_info_list = []
    for user_log in user_logs:
        user_log_info_list.append(pack_user_log_info(user_log=user_log))

    return user_log_info_list
