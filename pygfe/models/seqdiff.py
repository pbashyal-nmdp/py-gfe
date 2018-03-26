# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from pygfe.models.base_model_ import Model
from pygfe import util


class Seqdiff(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, term: str=None, rank: int=None, location: str=None, ref: str=None, inseq: str=None):  # noqa: E501
        """Seqdiff - a model defined in Swagger

        :param term: The term of this Seqdiff.  # noqa: E501
        :type term: str
        :param rank: The rank of this Seqdiff.  # noqa: E501
        :type rank: int
        :param location: The location of this Seqdiff.  # noqa: E501
        :type location: str
        :param ref: The ref of this Seqdiff.  # noqa: E501
        :type ref: str
        :param inseq: The inseq of this Seqdiff.  # noqa: E501
        :type inseq: str
        """
        self.swagger_types = {
            'term': str,
            'rank': int,
            'location': str,
            'ref': str,
            'inseq': str
        }

        self.attribute_map = {
            'term': 'term',
            'rank': 'rank',
            'location': 'location',
            'ref': 'ref',
            'inseq': 'inseq'
        }

        self._term = term
        self._rank = rank
        self._location = location
        self._ref = ref
        self._inseq = inseq

    @classmethod
    def from_dict(cls, dikt) -> 'Seqdiff':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Seqdiff of this Seqdiff.  # noqa: E501
        :rtype: Seqdiff
        """
        return util.deserialize_model(dikt, cls)

    @property
    def term(self) -> str:
        """Gets the term of this Seqdiff.


        :return: The term of this Seqdiff.
        :rtype: str
        """
        return self._term

    @term.setter
    def term(self, term: str):
        """Sets the term of this Seqdiff.


        :param term: The term of this Seqdiff.
        :type term: str
        """

        self._term = term

    @property
    def rank(self) -> int:
        """Gets the rank of this Seqdiff.


        :return: The rank of this Seqdiff.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank: int):
        """Sets the rank of this Seqdiff.


        :param rank: The rank of this Seqdiff.
        :type rank: int
        """

        self._rank = rank

    @property
    def location(self) -> str:
        """Gets the location of this Seqdiff.


        :return: The location of this Seqdiff.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """Sets the location of this Seqdiff.


        :param location: The location of this Seqdiff.
        :type location: str
        """

        self._location = location

    @property
    def ref(self) -> str:
        """Gets the ref of this Seqdiff.


        :return: The ref of this Seqdiff.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref: str):
        """Sets the ref of this Seqdiff.


        :param ref: The ref of this Seqdiff.
        :type ref: str
        """

        self._ref = ref

    @property
    def inseq(self) -> str:
        """Gets the inseq of this Seqdiff.


        :return: The inseq of this Seqdiff.
        :rtype: str
        """
        return self._inseq

    @inseq.setter
    def inseq(self, inseq: str):
        """Sets the inseq of this Seqdiff.


        :param inseq: The inseq of this Seqdiff.
        :type inseq: str
        """

        self._inseq = inseq
