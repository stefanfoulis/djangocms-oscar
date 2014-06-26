from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from django.db import models

from .models import FeaturedProduct
from oscar.apps.dashboard.catalogue.widgets import ProductSelect


class FeaturedProductPlugin(CMSPluginBase):
    """
    Displays a selected product from oscar.
    """
    model = FeaturedProduct
    name = _('Featured Product')
    admin_preview = True
    render_template = 'djangocms_oscar/product_plugin.html'

    def render(self, context, instance, placeholder):
        return context



plugin_pool.register_plugin(FeaturedProductPlugin)
