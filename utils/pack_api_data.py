from Order.models import Order
from Supplier.models import Supplier
from Item.models import Item
from Item.models import TechnicalChange


def pack_order_info(order: Order):
    """ 打包订单信息
    """
    return {
        "order_id": order.id,
        "order_num": order.order_num,
        "order_status": order.order_status,
        "order_start_time": str(order.order_start_time),
    }


def pack_order_info_list(orders: list[Order]):
    """ 打包订单信息列表
    """
    order_info_list = []
    for order in orders:
        order_info_list.append(pack_order_info(order=order))
    
    return order_info_list


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
    return {
        "item_id": item.id,
        "name": item.name,
    }


def pack_item_info_list(items: list[Item]):
    """ 打包物品信息列表
    """
    item_info_list = []
    for item in items:
        item_info_list.append(pack_item_info(item=item))
    
    return item_info_list


def pack_technical_change_info(technical_change: TechnicalChange):
    """ 打包技术变更信息
    """
    return {
        "technical_change_id": technical_change.id,
        "name": technical_change.name,
    }


def pack_technical_change_info_list(technical_changes: list[TechnicalChange]):
    """ 打包技术变更信息列表
    """
    technical_change_info_list = []
    for technical_change in technical_changes:
        technical_change_info_list.append(pack_technical_change_info(technical_change=technical_change))
    
    return technical_change_info_list
