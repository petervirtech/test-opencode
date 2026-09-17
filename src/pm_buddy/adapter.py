"""
Azure DevOps adapter for PM Buddy (hybrid stub).

Only contains stubs – it can be extended to sync with TFS.
"""

from .database import DB


class AzureAdapter:
    def __init__(self, db: DB):
        self.db = db
        # In a real implementation we would store credentials and endpoints.

    def sync_to_azure(self) -> None:
        """
        Placeholder for hybrid sync logic.
        Would iterate over local entities, compare with Azure DevOps work items,
        create or update as necessary.
        """
        pass

    def sync_from_azure(self) -> None:
        """
        Placeholder for pulling latest state from Azure DevOps.
        """
        pass
