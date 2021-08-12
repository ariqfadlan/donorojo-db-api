"""database seeds

Revision ID: dcd2ee504ec0
Revises: a6c448d0edcd
Create Date: 2021-08-12 10:36:41.035751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcd2ee504ec0'
down_revision = 'a6c448d0edcd'
branch_labels = None
depends_on = None

tourist_attraction_table = sa.table('tourist_attraction',
        sa.column('id', sa.Integer),
        sa.column('name', sa.String),
        sa.column('category', sa.String)
    )


def upgrade():
    data_upgrades()

def downgrade():
    data_downgrades()

def data_upgrades():
    op.bulk_insert(tourist_attraction_table,
        [
            {"id":1, "name": "Bukit Ngiroboyo", "category": "bukit"},
            {"id":2, "name": "Bukit Pring Jono", "category": "bukit"},
            {"id":3, "name": "Gemulung View", "category": "bukit,pantai,tebing"},
            {"id":4, "name": "Goa Kalak", "category": "goa"},
            {"id":5, "name": "New Asgard", "category": "pantai,tebing"},
            {"id":6, "name": "Pantai Karang Bolong", "category": "pantai"},
            {"id":7, "name": "Pantai Klayar", "category": "pantai"},
            {"id":8, "name": "Pantai Ngareng-areng", "category": "pantai"},
            {"id":9, "name": "Pantai Ngiroboyo", "category": "pantai"},
            {"id":10, "name": "Tanjung Klayar", "category": "pantai"},
            {"id":11,"name":  "Tebing Klothok", "category": "tebing"},
            {"id":12,"name":  "Tebing Panjang", "category": "tebing"},
            {"id":13,"name":  "Goa Jenggung", "category": "goa"},
            {"id":14,"name":  "Goa Luweng Ombo", "category": "goa"},
            {"id":15,"name":  "Pantai Buyutan", "category": "pantai"},
            {"id":16,"name":  "Pantai Ngandul", "category": "pantai"},
            {"id":17,"name":  "Pantai Ngobyogan", "category": "pantai"},
            {"id":18,"name":  "Pantai Pisher", "category": "pantai"},
            {"id":19,"name":  "Pantai Seruni", "category": "pantai"}
            ]
        )

def data_downgrades():
    op.execute("DELETE FROM tourist_attraction")

