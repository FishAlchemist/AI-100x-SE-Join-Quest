from enum import Enum, auto


class PromotionType(str, Enum):
    THRESHOLD_DISCOUNT = "threshold_discount"
    BOGO_COSMETICS = "bogo_cosmetics"
    DOUBLE_11 = "double_11_promotion"





class ProductCategory(str, Enum):
    COSMETICS = "cosmetics"
    APPAREL = "apparel"
    DEFAULT = ""
