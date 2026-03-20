from sqlalchemy import Column, Integer, String, ForeignKey, Float, Enum, Table
from sqlalchemy.orm import relationship, declarative_base
import enum

Base = declarative_base()

class Accreditation(enum.Enum):
    NU_NR = "NATO Unclassified / NATO Restricted"
    NS = "NATO Secret"

class CIStatus(enum.Enum):
    ACTIVE = "Active"
    UNDER_REPAIR = "Under Repair"
    DECOMMISSIONED = "Decommissioned"
    PLANNED = "Planned"

class RelationshipType(enum.Enum):
    DEPENDS_ON = "Depends On"
    CONNECTED_TO = "Connected To"
    HOSTED_ON = "Hosted On"

class Zone(Base):
    __tablename__ = 'zones'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    countries = relationship("Country", back_populates="zone")

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    zone_id = Column(Integer, ForeignKey('zones.id'))
    zone = relationship("Zone", back_populates="countries")
    locations = relationship("Location", back_populates="country")

class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    country_id = Column(Integer, ForeignKey('countries.id'))
    country = relationship("Country", back_populates="locations")
    enclaves = relationship("Enclave", back_populates="location")

class Enclave(Base):
    __tablename__ = 'enclaves'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    accreditation = Column(Enum(Accreditation), nullable=False)
    location_id = Column(Integer, ForeignKey('locations.id'))
    location = relationship("Location", back_populates="enclaves")
    networks = relationship("Network", back_populates="enclave")

class Network(Base):
    __tablename__ = 'networks'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    vlan = Column(String)
    subnet = Column(String)
    enclave_id = Column(Integer, ForeignKey('enclaves.id'))
    enclave = relationship("Enclave", back_populates="networks")
    cis = relationship("ConfigurationItem", back_populates="network")

class ConfigurationItem(Base):
    __tablename__ = 'configuration_items'
    id = Column(Integer, primary_key=True)
    hostname = Column(String, unique=True, nullable=False)
    device_type = Column(String) # Switch, Router, Firewall, etc.
    status = Column(Enum(CIStatus), default=CIStatus.ACTIVE)
    
    # Hardware Specs
    is_virtual = Column(Integer, default=0) # 0: Physical, 1: Virtual
    cpu = Column(String)
    ram_gb = Column(Integer)
    disk_gb = Column(Integer)
    
    # Networking
    ip_address = Column(String)
    mac_address = Column(String)
    
    # Software
    os = Column(String)
    functions = Column(String)
    
    network_id = Column(Integer, ForeignKey('networks.id'))
    network = relationship("Network", back_populates="cis")

class Relationship(Base):
    __tablename__ = 'relationships'
    id = Column(Integer, primary_key=True)
    source_ci_id = Column(Integer, ForeignKey('configuration_items.id'))
    target_ci_id = Column(Integer, ForeignKey('configuration_items.id'))
    rel_type = Column(Enum(RelationshipType), nullable=False)
