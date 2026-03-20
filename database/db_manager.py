from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Zone, Country, Location, Enclave, Network, ConfigurationItem, Accreditation, CIStatus

DB_URL = "sqlite:///cmdb_storage.db"

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
    seed_data()

import random

def seed_data():
    db = SessionLocal()
    
    # 1. Base Zones and Countries (ensure they exist)
    zones_data = {
        "Europe": ["Albania", "Belgium", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden", "Türkiye", "United Kingdom"],
        "North America": ["United States", "Canada"]
    }
    
    for zone_name, country_list in zones_data.items():
        zone = db.query(Zone).filter_by(name=zone_name).first()
        if not zone:
            zone = Zone(name=zone_name); db.add(zone); db.flush()
        for c_name in country_list:
            if not db.query(Country).filter_by(name=c_name).first():
                db.add(Country(name=c_name, zone=zone))
    db.commit()

    # 2. Strategic NATO Bases (Locations)
    nato_bases = {
        "Belgium": [("Brussels", 50.8, 4.3, "BR"), ("Mons", 50.4, 3.9, "MS")],
        "Netherlands": [("Brunssum", 50.9, 5.9, "HB"), ("The Hague", 52.0, 4.3, "TG")],
        "Italy": [("Naples", 40.8, 14.2, "NP"), ("Sigonella", 37.4, 14.9, "SG")],
        "Germany": [("Ramstein", 49.4, 7.5, "RS"), ("Ulm", 48.4, 9.9, "UL")],
        "United States": [("Norfolk", 36.8, -76.2, "NF")],
        "Spain": [("Torrejon", 40.4, -3.4, "TJ"), ("Betera", 39.5, -0.4, "BT")]
    }

    device_types = ["Server", "Router", "Firewall", "Switch", "Laptop", "Desktop", "Printer", "Scanner"]
    os_options = ["Windows Server 2022", "RHEL 9", "Ubuntu 22.04 LTS", "Windows 11", "Cisco IOS", "Junos OS"]

    for c_name, bases in nato_bases.items():
        country = db.query(Country).filter_by(name=c_name).first()
        if not country: continue
        
        for b_name, lat, lon, loc_code in bases:
            loc = db.query(Location).filter_by(name=b_name, country_id=country.id).first()
            if not loc:
                loc = Location(name=b_name, latitude=lat, longitude=lon, country=country)
                db.add(loc); db.flush()
            
            # 3. Create 4 Enclaves per Location (2 NR, 2 NS)
            enclave_configs = [
                ("NR", Accreditation.NU_NR, f"{loc_code}1"),
                ("NR", Accreditation.NU_NR, f"{loc_code}2"),
                ("NS", Accreditation.NS, f"{loc_code}3"),
                ("NS", Accreditation.NS, f"{loc_code}4")
            ]
            
            for prefix, acc, enc_code in enclave_configs:
                enc_name = f"{prefix}-CYS-{enc_code}"
                enclave = db.query(Enclave).filter_by(name=enc_name, location_id=loc.id).first()
                if not enclave:
                    enclave = Enclave(name=enc_name, accreditation=acc, location_id=loc.id)
                    db.add(enclave); db.flush()
                
                # 4. Create 3 Networks per Enclave
                subnets = ["192.168.1.0/24", "10.0.0.1/24", "172.16.0.0/24"]
                for i, sn in enumerate(subnets):
                    net_name = f"Net-{i+1}-{prefix}"
                    network = db.query(Network).filter_by(name=net_name, enclave_id=enclave.id).first()
                    if not network:
                        network = Network(name=net_name, vlan=str(100+i), subnet=sn, enclave_id=enclave.id)
                        db.add(network); db.flush()
                        
                        # 5. Populate 50 CIs per Network with Randomized Server Placement
                        for seq in range(1, 51):
                            is_v = random.choice([True, False])
                            p_v = "V" if is_v else "P"
                            hostname = f"{prefix}CYS{enc_code}{p_v}{str(seq).zfill(3)}"
                            
                            if not db.query(ConfigurationItem).filter_by(hostname=hostname).first():
                                # Randomize device type, but ensure at least some diversity
                                if seq % 10 == 0: dev_type = "Server"
                                elif seq % 10 == 1: dev_type = "Router"
                                elif seq % 10 == 2: dev_type = "Firewall"
                                else: dev_type = random.choice(device_types)
                                
                                new_ci = ConfigurationItem(
                                    hostname=hostname,
                                    device_type=dev_type,
                                    status=CIStatus.ACTIVE,
                                    is_virtual=1 if is_v else 0,
                                    cpu="Xeon E-2300" if dev_type == "Server" else "Core i7",
                                    ram_gb=64 if dev_type == "Server" else 16,
                                    disk_gb=2000 if dev_type == "Server" else 512,
                                    ip_address=f"{sn.rsplit('.', 1)[0]}.{seq+10}",
                                    os=random.choice(os_options),
                                    network_id=network.id
                                )
                                db.add(new_ci)
                    db.commit()

    db.close()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
