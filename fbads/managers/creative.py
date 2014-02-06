# coding: utf-8
from fbads.managers.base import Manager
from fbads.resources.creative import CreativeResource


class CreativeManager(Manager):
    resource_class = CreativeResource
    resource_name = 'adcreatives'

    def _get_api_path(self, object_id):
        return '{0}'.format(object_id)

    def add(self, title, body, link_url, image_url, related_fan_page=None):
        assert len(body) <= 90, u'text must be 90 chars or less'

        payload = {
            'title': title,
            'body': body,
            'link_url': link_url,
            'image_url': image_url,
        }

        if related_fan_page:
            payload.update({
                'related_fan_page': related_fan_page,
            })

        content = super(CreativeManager, self).add(
            payload=payload,
        )

        return content['id']
