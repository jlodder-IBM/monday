from ..query_joins import get_tags_query
from .base import BaseResource


class TagResource(BaseResource):
    def fetch_tags(self, tag_ids=None):
        query = get_tags_query(tag_ids)
        return self.client.execute(query)

