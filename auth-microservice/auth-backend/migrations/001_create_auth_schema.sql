-- Create schema
CREATE SCHEMA IF NOT EXISTS auth;

-- Users table
CREATE TABLE IF NOT EXISTS auth.users (
    id SERIAL PRIMARY KEY,
    auth0_id VARCHAR(128) UNIQUE NOT NULL,
    email VARCHAR(255) NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    cell_number VARCHAR(32),
    landline_number VARCHAR(32),
    created_by INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    status VARCHAR(64) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS auth.companies (
    id SERIAL PRIMARY KEY,
    identifier VARCHAR(128) UNIQUE NOT NULL,
    identifier_type VARCHAR(128),   
    email VARCHAR(255) NOT NULL,
    company_name VARCHAR(255),
    legal_name VARCHAR(255),
    address_line_1 VARCHAR(255),
    address_line_2 VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    postal_code VARCHAR(255),
    country VARCHAR(255),
    phone_number VARCHAR(255),
    contact_name VARCHAR(255),
    contact_email VARCHAR(255),
    contact_phone VARCHAR(255), 
    website VARCHAR(255),
    industry VARCHAR(255),
    description TEXT,
    created_by INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    status VARCHAR(64) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Roles table
CREATE TABLE IF NOT EXISTS auth.roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) UNIQUE NOT NULL,
    description TEXT,
    created_by INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    status VARCHAR(64) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Permissions table
CREATE TABLE IF NOT EXISTS auth.permissions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) UNIQUE NOT NULL,
    description TEXT,
    created_by INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    status VARCHAR(64) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- User Roles table
CREATE TABLE IF NOT EXISTS auth.user_roles (
    user_id INTEGER REFERENCES auth.users(id) ON DELETE CASCADE,
    role_id INTEGER REFERENCES auth.roles(id) ON DELETE CASCADE,
    created_by INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    status VARCHAR(64) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (user_id, role_id)
);

-- Role Permissions table
CREATE TABLE IF NOT EXISTS auth.role_permissions (
    role_id INTEGER REFERENCES auth.roles(id) ON DELETE CASCADE,
    permission_id INTEGER REFERENCES auth.permissions(id) ON DELETE CASCADE,
    created_by INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    status VARCHAR(64) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (role_id, permission_id)
);

-- Seed roles
INSERT INTO auth.roles (name, description) VALUES
  ('admin', 'Administrator with full access'),
  ('manager', 'Manager with limited access'),
  ('viewer', 'Viewer with read-only access')
ON CONFLICT (name) DO NOTHING;

-- Seed permissions
INSERT INTO auth.permissions (name, description) VALUES
  ('manage_users', 'Can manage users'),
  ('view_reports', 'Can view reports')
ON CONFLICT (name) DO NOTHING;

-- Assign permissions to roles (example)
INSERT INTO auth.role_permissions (role_id, permission_id)
SELECT r.id, p.id
FROM auth.roles r, auth.permissions p
WHERE (r.name = 'admin' AND p.name IN ('manage_users', 'view_reports'))
   OR (r.name = 'manager' AND p.name = 'view_reports')
ON CONFLICT DO NOTHING;

CREATE TABLE IF NOT EXISTS auth.phy_address (
    id SERIAL PRIMARY KEY,
    company_id INTEGER REFERENCES auth.companies(id) ON DELETE CASCADE,
    address_line_1 VARCHAR(255),
    address_line_2 VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    postal_code VARCHAR(255),
    country VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    status VARCHAR(64) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS auth.mail_address (
    id SERIAL PRIMARY KEY,
    company_id INTEGER REFERENCES auth.companies(id) ON DELETE CASCADE,
    address_line_1 VARCHAR(255),
    address_line_2 VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    postal_code VARCHAR(255),
    country VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    status VARCHAR(64) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS auth.company_contacts (
    id SERIAL PRIMARY KEY,
    company_id INTEGER REFERENCES auth.companies(id) ON DELETE CASCADE,
    contact_name VARCHAR(255),
    contact_email VARCHAR(255),
    contact_phone VARCHAR(255),
    role VARCHAR(128),
    is_active BOOLEAN DEFAULT TRUE,
    status VARCHAR(64) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
); 