from Item.models import Item
from Order.models import Order


def calc_item_children_total_data(item: Item):
    """ 计算物品子节点相关所有总数据
    总成本
    销售总价
    """
    total_cost = item.cost
    total_sell_price = item.sell_price

    queue = list(item.item_set.all())
    while queue:
        for item in queue:
            total_cost += item.cost
            total_sell_price += item.sell_price

        next_queue = []
        for item in queue:
            next_queue.extend(item.item_set.all())
        queue = next_queue

    return {
        "total_cost": total_cost,
        "total_sell_price": total_sell_price,
    }


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


def calc_item_total_num(item: Item):
    """ 计算物品总数量
    上级物品数量会影响下级物品总数量
    """
    total_num = item.num
    parent_item = item.parent_item
    # 往上追溯，一直到没有上级物品，累乘数量
    while parent_item:
        total_num *= parent_item.num
        # 追溯
        parent_item = parent_item.parent_item
    return total_num
