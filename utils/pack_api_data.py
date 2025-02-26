from Order.models import Order


def pack_order_info(order: Order):
    """ 打包订单信息
    """
    return {
        "id": order.id,
        "order_num": order.order_num,
        "order_status": order.order_status,
        "order_start_time": order.order_start_time,
    }


def pack_order_info_list(orders: list[Order]):
    """ 打包订单信息列表
    """
    order_info_list = []
    for order in orders:
        order_info_list.append(pack_order_info(order=order))
    
    return order_info_list
