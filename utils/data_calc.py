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


def calc_item_level(item: Item):
    """ 计算物品层级
    """
    level = 1
    
    while item.parent_item:
        item = item.parent_item
        level += 1
    
    return level


def check_item_circle_quote(item: Item):
    """ 检查物品循环引用
    """
    appeared_item_set = {item}  # 记录出现过的物品set
    while item.parent_item:
        if item.parent_item in appeared_item_set:
            return False  # 出现了重复元素，判定为重复引用
        # 加入记录
        appeared_item_set.add(item.parent_item)
        # 取上层物品为当前物品
        item = item.parent_item
    # 成功结束，没有循环引用
    return True
