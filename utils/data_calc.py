from Item.models import Item
from Order.models import Order


def calc_item_total_cost(item: Item):
    """ 计算物品总成本
    """
    total = item.cost

    queue = list(item.item_set.all())
    while queue:
        level_total = sum(item.cost for item in queue)
        total += level_total
        next_queue = []
        for item in queue:
            next_queue.extend(item.item_set.all())
        queue = next_queue

    return total


def calc_order_total_cost(order: Order):
    """ 计算订单总成本
    """
    items = order.item_set.all()

    total = 0

    for item in items:
        total += item.cost

    return total
