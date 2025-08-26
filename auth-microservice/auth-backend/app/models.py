from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, Text
from .database import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth"}
    id = Column(Integer, primary_key=True, index=True)
    auth0_id = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    cell_number = Column(String(32))
    landline_number = Column(String(32))
    created_by = Column(Integer)
    is_active = Column(Boolean, default=True)
    status = Column(String(64), default="active")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Company(Base):
    __tablename__ = "companies"
    __table_args__ = {"schema": "auth"}
    id = Column(Integer, primary_key=True, index=True)
    identifier = Column(String(128), unique=True, nullable=False)
    identifier_type = Column(String(128))
    email = Column(String, nullable=False)
    company_name = Column(String)
    legal_name = Column(String)
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    country = Column(String)
    phone_number = Column(String)
    contact_name = Column(String)
    contact_email = Column(String)
    contact_phone = Column(String)
    website = Column(String)
    industry = Column(String)
    description = Column(Text)
    created_by = Column(Integer)
    is_active = Column(Boolean, default=True)
    status = Column(String(64), default="active")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Role(Base):
    __tablename__ = "roles"
    __table_args__ = {"schema": "auth"}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), unique=True, nullable=False)
    description = Column(Text)
    created_by = Column(Integer)
    is_active = Column(Boolean, default=True)
    status = Column(String(64), default="active")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Permission(Base):
    __tablename__ = "permissions"
    __table_args__ = {"schema": "auth"}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), unique=True, nullable=False)
    description = Column(Text)
    created_by = Column(Integer)
    is_active = Column(Boolean, default=True)
    status = Column(String(64), default="active")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class UserRole(Base):
    __tablename__ = "user_roles"
    __table_args__ = {"schema": "auth"}
    user_id = Column(Integer, ForeignKey("auth.users.id"), primary_key=True)
    role_id = Column(Integer, ForeignKey("auth.roles.id"), primary_key=True)
    created_by = Column(Integer)
    is_active = Column(Boolean, default=True)
    status = Column(String(64), default="active")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class RolePermission(Base):
    __tablename__ = "role_permissions"
    __table_args__ = {"schema": "auth"}
    role_id = Column(Integer, ForeignKey("auth.roles.id"), primary_key=True)
    permission_id = Column(Integer, ForeignKey("auth.permissions.id"), primary_key=True)
    created_by = Column(Integer)
    is_active = Column(Boolean, default=True)
    status = Column(String(64), default="active")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class PhyAddress(Base):
    __tablename__ = "phy_address"
    __table_args__ = {"schema": "auth"}
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("auth.companies.id"))
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    country = Column(String)
    is_active = Column(Boolean, default=True)
    status = Column(String(64), default="active")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class MailAddress(Base):
    __tablename__ = "mail_address"
    __table_args__ = {"schema": "auth"}
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("auth.companies.id"))
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    country = Column(String)
    is_active = Column(Boolean, default=True)
    status = Column(String(64), default="active")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class CompanyContact(Base):
    __tablename__ = "company_contacts"
    __table_args__ = {"schema": "auth"}
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("auth.companies.id"))
    contact_name = Column(String)
    contact_email = Column(String)
    contact_phone = Column(String)
    role = Column(String(128))
    is_active = Column(Boolean, default=True)
    status = Column(String(64), default="active")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())