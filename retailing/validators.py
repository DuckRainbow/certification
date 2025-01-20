from rest_framework.serializers import ValidationError


class SupplierValidator:
    """
    Данный валидатор проверяет, чтобы при создании поставщика, его уровень был больше(ниже по иерархии),
    чем уровень его поставщика
    """

    def __init__(self, field1, field2):
        self.level = field1
        self.supplier = field2

    def __call__(self):
        if self.supplier:
            if self.level <= self.supplier.level:
                raise ValidationError('Уровень должен быть больше уровня поставщика.')
        return None
