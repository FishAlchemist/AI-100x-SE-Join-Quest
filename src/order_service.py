from src.entities import Order, OrderItem

class OrderService:
    def __init__(self, **kwargs):
        self.threshold_discount = kwargs.get('threshold_discount')
        self.bogo_type = kwargs.get('bogo_type')

    def _apply_promotions(self, items: list[OrderItem]) -> tuple[list[OrderItem], int, int, int]:
        processed_items = []
        original_amount = 0

        for item in items:
            original_amount += item.product.unit_price * item.quantity
            if item.product.category == "cosmetics" and self.bogo_type:
                if self.bogo_type == 'buy_one_get_one':
                    processed_items.append(OrderItem(product=item.product, quantity=item.quantity * 2))
                elif self.bogo_type == 'buy_two_get_one':
                    free_quantity = item.quantity // 2
                    processed_items.append(OrderItem(product=item.product, quantity=item.quantity + free_quantity))
            else:
                processed_items.append(item)
        
        total_amount = original_amount
        discount = 0

        # Apply threshold discount
        if self.threshold_discount:
            if original_amount >= self.threshold_discount['threshold']:
                discount = self.threshold_discount['discount']
                total_amount -= discount
        
        return processed_items, original_amount, discount, total_amount

    def checkout(self, items: list[OrderItem]) -> Order:
        processed_items, original_amount, discount, total_amount = self._apply_promotions(items)

        return Order(items=processed_items, original_amount=original_amount, discount=discount, total_amount=total_amount)