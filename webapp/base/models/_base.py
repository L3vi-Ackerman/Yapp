from base.models._timestamp import Timestamps
from base.models._uuid import UUIDModel


class AbstractBaseModel(UUIDModel, Timestamps):
    class Meta:
        abstract = True
