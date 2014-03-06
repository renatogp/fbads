# coding: utf-8
import hashlib
import json
from fbads.managers.base import Manager
from fbads.resources.customaudience import CustomAudienceResource  # CustomAudienceUserResource


class CustomAudienceManager(Manager):
    resource_class = CustomAudienceResource
    resource_name = 'customaudiences'

    def _get_api_path(self, object_id):
        return '{0}'.format(object_id)

    def _delete_api_path(self, object_id):
        return '{0}'.format(object_id)

    def add_users(self, customaudience_id, facebook_ids=[], emails=[]):
        assert not facebook_ids or 0 < len(facebook_ids) < 10000, u'facebook_ids len must be between 1 and 10000'
        assert not emails or 0 < len(emails) < 10000, u'emails len must be between 1 and 10000'
        assert facebook_ids and not emails or emails and not facebook_ids

        users = []
        for facebook_id in facebook_ids:
            users.append({'id': facebook_id})

        for email in emails:
            m = hashlib.md5()
            m.update(email)
            email_hash = m.hexdigest()
            users.append({'email_hash': email_hash})

        return super(CustomAudienceManager, self).add(
            payload={
                'users': json.dumps(users),
                'hash_type': 'md5',
            },
            api_path='{0}/users'.format(customaudience_id)
        )

    def delete_users(self, customaudience_id, facebook_ids=[], emails=[]):
        #TODO: missing docs
        assert not facebook_ids or 0 < len(facebook_ids) < 10000, u'facebook_ids len must be between 1 and 10000'
        assert not emails or 0 < len(emails) < 10000, u'emails len must be between 1 and 10000'
        assert facebook_ids and not emails or emails and not facebook_ids

        users = []
        for facebook_id in facebook_ids:
            users.append({'id': facebook_id})

        for email in emails:
            m = hashlib.md5()
            m.update(email)
            email_hash = m.hexdigest()
            users.append({'email_hash': email_hash})

        return super(CustomAudienceManager, self).delete(
            object_id=None,  # explain why later...
            payload={
                'users': json.dumps(users),
                'hash_type': 'md5',
            },
            api_path='{0}/users'.format(customaudience_id)
        )

    def add(self, name, description=None, opt_out_link=None):
        payload = {
            'name': name,
            'description': description,
            'opt_out_link': opt_out_link,
        }

        content = super(CustomAudienceManager, self).add(
            payload=payload
        )

        return content['id']
