# coding: utf-8

"""
    Phenopolis API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: info@phenopolis.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.hpo import HPO  # noqa: F401,E501
from swagger_client.models.variant import Variant  # noqa: F401,E501


class Patient(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'phenotypes': 'HPO',
        'variants': 'Variant'
    }

    attribute_map = {
        'id': 'id',
        'phenotypes': 'phenotypes',
        'variants': 'variants'
    }

    def __init__(self, id=None, phenotypes=None, variants=None):  # noqa: E501
        """Patient - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._phenotypes = None
        self._variants = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if phenotypes is not None:
            self.phenotypes = phenotypes
        if variants is not None:
            self.variants = variants

    @property
    def id(self):
        """Gets the id of this Patient.  # noqa: E501


        :return: The id of this Patient.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Patient.


        :param id: The id of this Patient.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def phenotypes(self):
        """Gets the phenotypes of this Patient.  # noqa: E501


        :return: The phenotypes of this Patient.  # noqa: E501
        :rtype: HPO
        """
        return self._phenotypes

    @phenotypes.setter
    def phenotypes(self, phenotypes):
        """Sets the phenotypes of this Patient.


        :param phenotypes: The phenotypes of this Patient.  # noqa: E501
        :type: HPO
        """

        self._phenotypes = phenotypes

    @property
    def variants(self):
        """Gets the variants of this Patient.  # noqa: E501


        :return: The variants of this Patient.  # noqa: E501
        :rtype: Variant
        """
        return self._variants

    @variants.setter
    def variants(self, variants):
        """Sets the variants of this Patient.


        :param variants: The variants of this Patient.  # noqa: E501
        :type: Variant
        """

        self._variants = variants

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Patient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
