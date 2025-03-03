from ..query_joins import get_groups_by_board_query, get_items_by_group_query, create_group_query, \
    duplicate_group_query, archive_group_query, delete_group_query
from .base import BaseResource


class GroupResource(BaseResource):
    def get_groups_by_board(self, board_ids):
        query = get_groups_by_board_query(board_ids=board_ids)
        return self.client.execute(query)

    def get_items_by_group(self, board_id, group_id, limit=None, cursor=None):
        query = get_items_by_group_query(board_id=board_id, group_id=group_id, limit=limit, cursor=cursor)
        return self.client.execute(query)

    def create_group(self, board_id, group_name):
        query = create_group_query(board_id=board_id, group_name=group_name)
        return self.client.execute(query)

    def duplicate_group(self, board_id, group_id):
        query = duplicate_group_query(board_id=board_id, group_id=group_id)
        return self.client.execute(query)

    def archive_group(self, board_id, group_id):
        query = archive_group_query(board_id=board_id, group_id=group_id)
        return self.client.execute(query)

    def delete_group(self, board_id, group_id):
        query = delete_group_query(board_id=board_id, group_id=group_id)
        return self.client.execute(query)
