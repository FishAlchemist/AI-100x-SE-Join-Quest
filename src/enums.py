from enum import Enum, auto


class PromotionType(str, Enum):
    THRESHOLD_DISCOUNT = "threshold_discount"
    BOGO_TYPE = "bogo_type"
    DOUBLE_11 = "double_11_promotion"


class BogoType(Enum):
    BUY_ONE_GET_ONE = auto()
    BUY_TWO_GET_ONE = auto()


class ProductCategory(str, Enum):
    COSMETICS = "cosmetics"
    APPAREL = "apparel"
    DEFAULT = ""
