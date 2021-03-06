
from django.db import models
from django.utils.translation import ugettext_lazy as _

from stock import constants


class Stock(models.Model):

    stock = models.IntegerField(_('Stock'), default=0)

    min_stock = models.IntegerField(_('Minimum stock'), default=0)

    def add_stock(self, value):

        self.validate_stock_value(value)

        self.stock += value
        self._commit_stock()

    def subtract_stock(self, value):

        self.validate_stock_value(value)

        if self.stock < value:
            raise ValueError(_('Not enough stock items'))

        self.stock -= value
        self._commit_stock()

    def validate_stock_value(self, value):

        if not isinstance(value, int):
            raise ValueError(_('Value should be integer'))

        if value < 1:
            raise ValueError(_('Value less then 1'))

    def _commit_stock(self):
        self.save(update_fields=['stock'])

    @property
    def has_stock(self):
        return self.stock > 0

    class Meta:
        abstract = True


class UnitType(models.Model):

    unit_type = models.CharField(
        _('Unit type'),
        max_length=100,
        choices=constants.UNIT_TYPES,
        default=constants.UNIT_TYPE_PCS)

    def format_qty(self, qty):
        return '{} {}'.format(qty, self.get_unit_type_display())

    class Meta:
        abstract = True
