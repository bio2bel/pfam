# -*- coding: utf-8 -*-

"""SQLAlchemy models for Bio2BEL Pfam."""

import logging

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

import pybel.dsl
from .constants import MODULE_NAME

__all__ = [
    'Base',
    'Family',
    'Clan'
]

logger = logging.getLogger(__name__)

FAMILY_TABLE_NAME = f'{MODULE_NAME}_family'
CLAN_TABLE_NAME = f'{MODULE_NAME}_clan'

Base: DeclarativeMeta = declarative_base()


class Family(Base):
    """A Pfam Protein Family."""

    __tablename__ = FAMILY_TABLE_NAME
    id = Column(Integer, primary_key=True)

    pfam_id = Column(String, nullable=False, index=True, unique=True)
    name = Column(String, nullable=True)
    summary = Column(String, nullable=True)

    bel_encoding = 'GRP'

    def as_pybel(self) -> pybel.dsl.Protein:
        """Serialize as a PyBEL protein."""
        return pybel.dsl.Protein(
            namespace=MODULE_NAME,
            name=self.name,
            identifier=self.pfam_id,
        )

    def __repr__(self):  # noqa: D105
        return f'Family(pfam_id={self.pfam_id}, name={self.name}, summary={self.summary})'


class Clan(Base):
    """A Pfam Protein Clan."""

    __tablename__ = CLAN_TABLE_NAME
    id = Column(Integer, primary_key=True)

    clan_id = Column(String, nullable=False, index=True, unique=True)
    name = Column(String, nullable=True)

    def as_pybel(self) -> pybel.dsl.Protein:
        """Serialize as a PyBEL protein."""
        return pybel.dsl.Protein(
            namespace='pfam.clan',
            name=self.name,
            identifier=self.clan_id,
        )

    def __repr__(self):  # noqa: D105
        return f'Clan(clan_id={self.clan_id}, name={self.name})'
