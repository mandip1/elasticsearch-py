from .utils import NamespacedClient, query_params


class RemoteClient(NamespacedClient):
    @query_params()
    async def info(self, params=None, headers=None):
        """
        `<http://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-remote-info.html>`_
        """
        return await self.transport.perform_request(
            "GET", "/_remote/info", params=params, headers=headers
        )