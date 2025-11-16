# Odoo 19 Community Edition

Custom Odoo 19 installation with custom modules and configurations.

## Setup

This project uses Docker Compose to run Odoo 19 with PostgreSQL.

### Prerequisites

- Docker
- Docker Compose

### Running the Application

```bash
docker compose up -d
```

### Accessing Odoo

- **URL**: https://odoo.automize.sa
- **Port**: 8069 (local access)

### Configuration

- Configuration file: `config/odoo.conf`
- Custom addons: `addons/`
- Master password is set in `config/odoo.conf`

### Database

- PostgreSQL 15
- Database name, user, and password are configured in `docker-compose.yml`

### Custom Modules

Place your custom Odoo modules in the `addons/` directory. They will be automatically loaded by Odoo.

## Project Structure

```
.
├── docker-compose.yml    # Docker Compose configuration
├── config/               # Odoo configuration files
│   └── odoo.conf        # Main Odoo configuration
├── addons/              # Custom Odoo modules/addons
└── README.md            # This file
```

## Development

After adding or modifying modules in the `addons/` directory:

1. Restart Odoo: `docker compose restart web`
2. Update the module list in Odoo (Apps > Update Apps List)
3. Install or upgrade your custom module

## Backup

To backup the database:
```bash
docker exec odoo-db-1 pg_dump -U odoo postgres > backup.sql
```

To restore:
```bash
cat backup.sql | docker exec -i odoo-db-1 psql -U odoo postgres
```
# CI/CD Pipeline Active
