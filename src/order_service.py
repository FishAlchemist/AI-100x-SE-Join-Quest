from src.entities import Order, OrderItem
from src.enums import ProductCategory, PromotionType


class OrderService:
    def __init__(self, **kwargs):
        self.threshold_discount_config = kwargs.get(
            PromotionType.THRESHOLD_DISCOUNT.value
        )
        self.bogo_cosmetics_promotion_active = kwargs.get(PromotionType.BOGO_COSMETICS.value)
        self.double_11_promotion_active = kwargs.get(
            PromotionType.DOUBLE_11.value, False
        )

    def _calculate_original_amount(self, items: list[OrderItem]) -> int:
        return sum(item.product.unit_price * item.quantity for item in items)

    def _apply_double_11_promotion(
        self, item: OrderItem, current_discount: int
    ) -> tuple[int, OrderItem]:
        if self.double_11_promotion_active and item.quantity >= 10:
            num_tens = item.quantity // 10
            discount_amount = num_tens * 10 * item.product.unit_price * 0.2
            return current_discount + int(discount_amount), item
        return current_discount, item

    def _apply_bogo_promotion(self, item: OrderItem) -> OrderItem:
        if item.product.category == ProductCategory.COSMETICS and self.bogo_cosmetics_promotion_active:
            return OrderItem(product=item.product, quantity=item.quantity + 1)
        return item

    def _apply_threshold_discount(
        self, original_amount: int, current_discount: int
    ) -> int:
        if self.threshold_discount_config:
            threshold = self.threshold_discount_config["threshold"]
            discount_value = self.threshold_discount_config["discount"]
            if original_amount >= threshold:
                return current_discount + discount_value
        return current_discount

    def checkout(self, items: list[OrderItem]) -> Order:
        original_amount = self._calculate_original_amount(items)
        total_discount = 0
        processed_items = []

        for item in items:
            # Apply Double 11 promotion
            total_discount, updated_item = self._apply_double_11_promotion(
                item, total_discount
            )

            # Apply BOGO promotion
            updated_item = self._apply_bogo_promotion(updated_item)

            processed_items.append(updated_item)

        # Apply Threshold discount
        total_discount = self._apply_threshold_discount(original_amount, total_discount)

        final_total_amount = original_amount - total_discount

        return Order(
            items=processed_items,
            original_amount=original_amount,
            discount=total_discount,
            total_amount=final_total_amount,
        )