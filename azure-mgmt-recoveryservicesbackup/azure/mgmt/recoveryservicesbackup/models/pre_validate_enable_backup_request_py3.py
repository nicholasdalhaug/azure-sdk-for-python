# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PreValidateEnableBackupRequest(Model):
    """Contract to validate if backup can be enabled on the given resource in a
    given vault and given configuration.
    It will validate followings
    1. Vault capacity
    2. VM is already protected
    3. Any VM related configuration passed in properties.

    :param resource_type: ProtectedItem Type- VM, SqlDataBase, AzureFileShare
     etc. Possible values include: 'Invalid', 'VM', 'FileFolder', 'AzureSqlDb',
     'SQLDB', 'Exchange', 'Sharepoint', 'VMwareVM', 'SystemState', 'Client',
     'GenericDataSource', 'SQLDataBase', 'AzureFileShare', 'SAPHanaDatabase'
    :type resource_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.DataSourceType
    :param resource_id: ARM Virtual Machine Id
    :type resource_id: str
    :param vault_id: ARM id of the Recovery Services Vault
    :type vault_id: str
    :param properties: Configuration of VM if any needs to be validated like
     OS type etc
    :type properties: str
    """

    _attribute_map = {
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'vault_id': {'key': 'vaultId', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'str'},
    }

    def __init__(self, *, resource_type=None, resource_id: str=None, vault_id: str=None, properties: str=None, **kwargs) -> None:
        super(PreValidateEnableBackupRequest, self).__init__(**kwargs)
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.vault_id = vault_id
        self.properties = properties