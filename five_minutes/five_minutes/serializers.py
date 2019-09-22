from rest_framework import serializers


class DynamicModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def get_field_names(self, declared_fields, info):
        field_names = super(DynamicModelSerializer, self).get_field_names(declared_fields, info)
        if self.dynamic_fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(self.dynamic_fields)
            excluded_field_names = set(field_names) - allowed
            field_names = tuple(x for x in field_names if x not in excluded_field_names)
        return field_names

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' or 'read_only_fields' arg up to the superclass
        self.dynamic_fields = kwargs.pop('fields', None)
        self.read_only_fields = kwargs.pop('read_only_fields', [])

        # Instantiate the superclass normally
        super(DynamicModelSerializer, self).__init__(*args, **kwargs)
