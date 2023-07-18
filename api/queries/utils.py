from sqlalchemy.orm import DeclarativeBase


def create_filters(model: DeclarativeBase, field_names: list[str], values: dict[str, any]) -> list[any]:
    """
    Create list of filters (with equal conditions) for given model and field_names
    
    Parameters:
    model: sqlalchemy model to create filters for
    field_names (list[str]): list containing names of fields to filter on
    values (dict[str, any]): dict containing values used to compare in new filters

    Returns:
    list[any]: list of sqlalchemy filters
    """
    check_field = {k: values.get(k) for k in field_names if values.get(k) is not None}
    conditions = [getattr(model, par).__eq__(val) for par, val in check_field.items()]
    return conditions
