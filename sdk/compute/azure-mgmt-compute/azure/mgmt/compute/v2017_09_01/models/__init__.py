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

try:
    from .resource_sku_capacity_py3 import ResourceSkuCapacity
    from .resource_sku_costs_py3 import ResourceSkuCosts
    from .resource_sku_capabilities_py3 import ResourceSkuCapabilities
    from .resource_sku_restriction_info_py3 import ResourceSkuRestrictionInfo
    from .resource_sku_restrictions_py3 import ResourceSkuRestrictions
    from .resource_sku_location_info_py3 import ResourceSkuLocationInfo
    from .resource_sku_py3 import ResourceSku
except (SyntaxError, ImportError):
    from .resource_sku_capacity import ResourceSkuCapacity
    from .resource_sku_costs import ResourceSkuCosts
    from .resource_sku_capabilities import ResourceSkuCapabilities
    from .resource_sku_restriction_info import ResourceSkuRestrictionInfo
    from .resource_sku_restrictions import ResourceSkuRestrictions
    from .resource_sku_location_info import ResourceSkuLocationInfo
    from .resource_sku import ResourceSku
from .resource_sku_paged import ResourceSkuPaged
from .compute_management_client_enums import (
    ResourceSkuCapacityScaleType,
    ResourceSkuRestrictionsType,
    ResourceSkuRestrictionsReasonCode,
)

__all__ = [
    'ResourceSkuCapacity',
    'ResourceSkuCosts',
    'ResourceSkuCapabilities',
    'ResourceSkuRestrictionInfo',
    'ResourceSkuRestrictions',
    'ResourceSkuLocationInfo',
    'ResourceSku',
    'ResourceSkuPaged',
    'ResourceSkuCapacityScaleType',
    'ResourceSkuRestrictionsType',
    'ResourceSkuRestrictionsReasonCode',
]