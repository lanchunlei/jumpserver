from django.utils.functional import cached_property
from django.db.models.fields.related_descriptors import (
    ManyToManyDescriptor, create_forward_many_to_many_manager
)


def create_asset_node_forward_many_to_many_manager(superclass, rel, reverse):
    Manager = create_forward_many_to_many_manager(superclass, rel, reverse)

    class AssetNodeManyRelatedManager(Manager):
        def set(self, objs, *, clear=False, through_defaults=None):
            ret = super().set(objs, clear=clear, through_defaults=through_defaults)
            print('--------------------set')
        set.alters_data = True

        def remove(self, *objs):
            ret = super().remove(*objs)
            print('--------------------remove')
        remove.alters_data = True
    return AssetNodeManyRelatedManager


class AssetNodeManyToManyDescriptor(ManyToManyDescriptor):
    @cached_property
    def related_manager_cls(self):
        related_model = self.rel.related_model if self.reverse else self.rel.model

        return create_asset_node_forward_many_to_many_manager(
            related_model._default_manager.__class__,
            self.rel,
            reverse=self.reverse,
        )
