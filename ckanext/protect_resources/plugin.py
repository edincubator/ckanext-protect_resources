import ckan.lib.base as base
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.common import _
from ckan.logic import side_effect_free
from ckan.logic.action import get

abort = base.abort


@side_effect_free
def resource_show(context, data_dict):
    if context.get('auth_user_obj', None) is None:
        return abort(403, _('You must be logged into EDI Data Catalogue for '
                            'downloading resources'))

    return get.resource_show(context, data_dict)


class Protect_ResourcesPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IActions)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'protect_resources')

    # IActions

    def get_actions(self):
        return {'resource_show': resource_show}
