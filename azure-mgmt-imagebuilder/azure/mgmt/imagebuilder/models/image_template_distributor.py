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


class ImageTemplateDistributor(Model):
    """Generic distribution object.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ImageTemplateManagedImageDistributor,
    ImageTemplateSharedImageDistributor, ImageTemplateVhdDistributor

    All required parameters must be populated in order to send to Azure.

    :param run_output_name: Required. The name to be used for the associated
     RunOutput.
    :type run_output_name: str
    :param artifact_tags: Tags that will be applied to the artifact once it
     has been created/updated by the distributor.
    :type artifact_tags: dict[str, str]
    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'run_output_name': {'required': True, 'pattern': r'^[A-Za-z0-9-_.]{1,64}$'},
        'type': {'required': True},
    }

    _attribute_map = {
        'run_output_name': {'key': 'runOutputName', 'type': 'str'},
        'artifact_tags': {'key': 'artifactTags', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'ManagedImage': 'ImageTemplateManagedImageDistributor', 'SharedImage': 'ImageTemplateSharedImageDistributor', 'VHD': 'ImageTemplateVhdDistributor'}
    }

    def __init__(self, **kwargs):
        super(ImageTemplateDistributor, self).__init__(**kwargs)
        self.run_output_name = kwargs.get('run_output_name', None)
        self.artifact_tags = kwargs.get('artifact_tags', None)
        self.type = None