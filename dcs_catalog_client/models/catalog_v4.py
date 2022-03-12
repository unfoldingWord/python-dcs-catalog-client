# coding: utf-8

"""
    Catalog Next API.

    This documentation describes the Catalog Next API for all versions and other miscellaneous endpoints.  # noqa: E501

    OpenAPI spec version: 1.16.3+dcs
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dcs_catalog_client.configuration import Configuration


class CatalogV4(object):
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
        'books': 'list[str]',
        'branch_or_tag_name': 'str',
        'id': 'int',
        'ingredients': 'list[object]',
        'lang_code': 'str',
        'metadata_api_contents_url': 'str',
        'metadata_json_url': 'str',
        'metadata_url': 'str',
        'metadata_version': 'str',
        'owner': 'str',
        'release_url': 'str',
        'released': 'datetime',
        'repo': 'str',
        'repo_url': 'str',
        'stage': 'str',
        'subject': 'str',
        'tarbar_url': 'str',
        'title': 'str',
        'url': 'str',
        'zipball_url': 'str'
    }

    attribute_map = {
        'books': 'books',
        'branch_or_tag_name': 'branch_or_tag_name',
        'id': 'id',
        'ingredients': 'ingredients',
        'lang_code': 'lang_code',
        'metadata_api_contents_url': 'metadata_api_contents_url',
        'metadata_json_url': 'metadata_json_url',
        'metadata_url': 'metadata_url',
        'metadata_version': 'metadata_version',
        'owner': 'owner',
        'release_url': 'release_url',
        'released': 'released',
        'repo': 'repo',
        'repo_url': 'repo_url',
        'stage': 'stage',
        'subject': 'subject',
        'tarbar_url': 'tarbar_url',
        'title': 'title',
        'url': 'url',
        'zipball_url': 'zipball_url'
    }

    def __init__(self, books=None, branch_or_tag_name=None, id=None, ingredients=None, lang_code=None, metadata_api_contents_url=None, metadata_json_url=None, metadata_url=None, metadata_version=None, owner=None, release_url=None, released=None, repo=None, repo_url=None, stage=None, subject=None, tarbar_url=None, title=None, url=None, zipball_url=None, _configuration=None):  # noqa: E501
        """CatalogV4 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._books = None
        self._branch_or_tag_name = None
        self._id = None
        self._ingredients = None
        self._lang_code = None
        self._metadata_api_contents_url = None
        self._metadata_json_url = None
        self._metadata_url = None
        self._metadata_version = None
        self._owner = None
        self._release_url = None
        self._released = None
        self._repo = None
        self._repo_url = None
        self._stage = None
        self._subject = None
        self._tarbar_url = None
        self._title = None
        self._url = None
        self._zipball_url = None
        self.discriminator = None

        if books is not None:
            self.books = books
        if branch_or_tag_name is not None:
            self.branch_or_tag_name = branch_or_tag_name
        if id is not None:
            self.id = id
        if ingredients is not None:
            self.ingredients = ingredients
        if lang_code is not None:
            self.lang_code = lang_code
        if metadata_api_contents_url is not None:
            self.metadata_api_contents_url = metadata_api_contents_url
        if metadata_json_url is not None:
            self.metadata_json_url = metadata_json_url
        if metadata_url is not None:
            self.metadata_url = metadata_url
        if metadata_version is not None:
            self.metadata_version = metadata_version
        if owner is not None:
            self.owner = owner
        if release_url is not None:
            self.release_url = release_url
        if released is not None:
            self.released = released
        if repo is not None:
            self.repo = repo
        if repo_url is not None:
            self.repo_url = repo_url
        if stage is not None:
            self.stage = stage
        if subject is not None:
            self.subject = subject
        if tarbar_url is not None:
            self.tarbar_url = tarbar_url
        if title is not None:
            self.title = title
        if url is not None:
            self.url = url
        if zipball_url is not None:
            self.zipball_url = zipball_url

    @property
    def books(self):
        """Gets the books of this CatalogV4.  # noqa: E501


        :return: The books of this CatalogV4.  # noqa: E501
        :rtype: list[str]
        """
        return self._books

    @books.setter
    def books(self, books):
        """Sets the books of this CatalogV4.


        :param books: The books of this CatalogV4.  # noqa: E501
        :type: list[str]
        """

        self._books = books

    @property
    def branch_or_tag_name(self):
        """Gets the branch_or_tag_name of this CatalogV4.  # noqa: E501


        :return: The branch_or_tag_name of this CatalogV4.  # noqa: E501
        :rtype: str
        """
        return self._branch_or_tag_name

    @branch_or_tag_name.setter
    def branch_or_tag_name(self, branch_or_tag_name):
        """Sets the branch_or_tag_name of this CatalogV4.


        :param branch_or_tag_name: The branch_or_tag_name of this CatalogV4.  # noqa: E501
        :type: str
        """

        self._branch_or_tag_name = branch_or_tag_name

    @property
    def id(self):
        """Gets the id of this CatalogV4.  # noqa: E501


        :return: The id of this CatalogV4.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CatalogV4.


        :param id: The id of this CatalogV4.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ingredients(self):
        """Gets the ingredients of this CatalogV4.  # noqa: E501


        :return: The ingredients of this CatalogV4.  # noqa: E501
        :rtype: list[object]
        """
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        """Sets the ingredients of this CatalogV4.


        :param ingredients: The ingredients of this CatalogV4.  # noqa: E501
        :type: list[object]
        """

        self._ingredients = ingredients

    @property
    def lang_code(self):
        """Gets the lang_code of this CatalogV4.  # noqa: E501


        :return: The lang_code of this CatalogV4.  # noqa: E501
        :rtype: str
        """
        return self._lang_code

    @lang_code.setter
    def lang_code(self, lang_code):
        """Sets the lang_code of this CatalogV4.


        :param lang_code: The lang_code of this CatalogV4.  # noqa: E501
        :type: str
        """

        self._lang_code = lang_code

    @property
    def metadata_api_contents_url(self):
        """Gets the metadata_api_contents_url of this CatalogV4.  # noqa: E501


        :return: The metadata_api_contents_url of this CatalogV4.  # noqa: E501
        :rtype: str
        """
        return self._metadata_api_contents_url

    @metadata_api_contents_url.setter
    def metadata_api_contents_url(self, metadata_api_contents_url):
        """Sets the metadata_api_contents_url of this CatalogV4.


        :param metadata_api_contents_url: The metadata_api_contents_url of this CatalogV4.  # noqa: E501
        :type: str
        """

        self._metadata_api_contents_url = metadata_api_contents_url

    @property
    def metadata_json_url(self):
        """Gets the metadata_json_url of this CatalogV4.  # noqa: E501


        :return: The metadata_json_url of this CatalogV4.  # noqa: E501
        :rtype: str
        """
        return self._metadata_json_url

    @metadata_json_url.setter
    def metadata_json_url(self, metadata_json_url):
        """Sets the metadata_json_url of this CatalogV4.


        :param metadata_json_url: The metadata_json_url of this CatalogV4.  # noqa: E501
        :type: str
        """

        self._metadata_json_url = metadata_json_url

    @property
    def metadata_url(self):
        """Gets the metadata_url of this CatalogV4.  # noqa: E501


        :return: The metadata_url of this CatalogV4.  # noqa: E501
        :rtype: str
        """
        return self._metadata_url

    @metadata_url.setter
    def metadata_url(self, metadata_url):
        """Sets the metadata_url of this CatalogV4.


        :param metadata_url: The metadata_url of this CatalogV4.  # noqa: E501
        :type: str
        """

        self._metadata_url = metadata_url

    @property
    def metadata_version(self):
        """Gets the metadata_version of this CatalogV4.  # noqa: E501


        :return: The metadata_version of this CatalogV4.  # noqa: E501
        :rtype: str
        """
        return self._metadata_version

    @metadata_version.setter
    def metadata_version(self, metadata_version):
        """Sets the metadata_version of this CatalogV4.


        :param metadata_version: The metadata_version of this CatalogV4.  # noqa: E501
        :type: str
        """

        self._metadata_version = metadata_version

    @property
    def owner(self):
        """Gets the owner of this CatalogV4.  # noqa: E501


        :return: The owner of this CatalogV4.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CatalogV4.


        :param owner: The owner of this CatalogV4.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def release_url(self):
        """Gets the release_url of this CatalogV4.  # noqa: E501


        :return: The release_url of this CatalogV4.  # noqa: E501
        :rtype: str
        """
        return self._release_url

    @release_url.setter
    def release_url(self, release_url):
        """Sets the release_url of this CatalogV4.


        :param release_url: The release_url of this CatalogV4.  # noqa: E501
        :type: str
        """

        self._release_url = release_url

    @property
    def released(self):
        """Gets the released of this CatalogV4.  # noqa: E501


        :return: The released of this CatalogV4.  # noqa: E501
        :rtype: datetime
        """
        return self._released

    @released.setter
    def released(self, released):
        """Sets the released of this CatalogV4.


        :param released: The released of this CatalogV4.  # noqa: E501
        :type: datetime
        """

        self._released = released

    @property
    def repo(self):
        """Gets the repo of this CatalogV4.  # noqa: E501


        :return: The repo of this CatalogV4.  # noqa: E501
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this CatalogV4.


        :param repo: The repo of this CatalogV4.  # noqa: E501
        :type: str
        """

        self._repo = repo

    @property
    def repo_url(self):
        """Gets the repo_url of this CatalogV4.  # noqa: E501


        :return: The repo_url of this CatalogV4.  # noqa: E501
        :rtype: str
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        """Sets the repo_url of this CatalogV4.


        :param repo_url: The repo_url of this CatalogV4.  # noqa: E501
        :type: str
        """

        self._repo_url = repo_url

    @property
    def stage(self):
        """Gets the stage of this CatalogV4.  # noqa: E501


        :return: The stage of this CatalogV4.  # noqa: E501
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this CatalogV4.


        :param stage: The stage of this CatalogV4.  # noqa: E501
        :type: str
        """

        self._stage = stage

    @property
    def subject(self):
        """Gets the subject of this CatalogV4.  # noqa: E501


        :return: The subject of this CatalogV4.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this CatalogV4.


        :param subject: The subject of this CatalogV4.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def tarbar_url(self):
        """Gets the tarbar_url of this CatalogV4.  # noqa: E501


        :return: The tarbar_url of this CatalogV4.  # noqa: E501
        :rtype: str
        """
        return self._tarbar_url

    @tarbar_url.setter
    def tarbar_url(self, tarbar_url):
        """Sets the tarbar_url of this CatalogV4.


        :param tarbar_url: The tarbar_url of this CatalogV4.  # noqa: E501
        :type: str
        """

        self._tarbar_url = tarbar_url

    @property
    def title(self):
        """Gets the title of this CatalogV4.  # noqa: E501


        :return: The title of this CatalogV4.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CatalogV4.


        :param title: The title of this CatalogV4.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def url(self):
        """Gets the url of this CatalogV4.  # noqa: E501


        :return: The url of this CatalogV4.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CatalogV4.


        :param url: The url of this CatalogV4.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def zipball_url(self):
        """Gets the zipball_url of this CatalogV4.  # noqa: E501


        :return: The zipball_url of this CatalogV4.  # noqa: E501
        :rtype: str
        """
        return self._zipball_url

    @zipball_url.setter
    def zipball_url(self, zipball_url):
        """Sets the zipball_url of this CatalogV4.


        :param zipball_url: The zipball_url of this CatalogV4.  # noqa: E501
        :type: str
        """

        self._zipball_url = zipball_url

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
        if issubclass(CatalogV4, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CatalogV4):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CatalogV4):
            return True

        return self.to_dict() != other.to_dict()
