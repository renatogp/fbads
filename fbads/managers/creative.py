# coding: utf-8
from fbads.managers.base import Manager
from fbads.resources.creative import CreativeResource


class CreativeManager(Manager):
    resource_class = CreativeResource
    resource_name = 'adcreatives'

    def _get_api_path(self, object_id):
        return '{0}'.format(object_id)

    def add(self, title, body, image_url, object_url=None, link_url=None, actor_id=None, related_fan_page=None):
        assert len(body) <= 90, u'text must be 90 chars or less'

        # making legacy code work with new ads api
        if link_url and not object_url:
            object_url = link_url

        if related_fan_page and not actor_id:
            actor_id = related_fan_page

        payload = {
            'title': title,
            'body': body,
            'object_url': object_url,
            'image_url': image_url,
        }

        if actor_id:
            payload.update({
                'actor_id': actor_id,
            })

        content = super(CreativeManager, self).add(
            payload=payload,
        )

        return content['id']
