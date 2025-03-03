from ..query_joins import get_complexity_query
from .base import BaseResource


class ComplexityResource(BaseResource):
    def get_complexity(self):
        query = get_complexity_query()
        return self.client.execute(query)
