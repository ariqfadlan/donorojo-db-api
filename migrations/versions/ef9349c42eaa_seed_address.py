"""seed address

Revision ID: ef9349c42eaa
Revises: dcd2ee504ec0
Create Date: 2021-08-12 13:16:25.651856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef9349c42eaa'
down_revision = 'dcd2ee504ec0'
branch_labels = None
depends_on = None

address_table = sa.table('address',
        sa.column('tourist_attraction_id', sa.Integer),
        sa.column('subvillage', sa.String),
        sa.column('village', sa.String),
        sa.column('district', sa.String),
        sa.column('regency', sa.String),
        sa.column('province', sa.String)
    )


def upgrade():
    op.bulk_insert(address_table,
        [
            {"tourist_attraction_id": 1, "subvillage": "Sambi", "village": "Sendang", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 2, "subvillage": "Sambi", "village": "Sendang", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 3, "subvillage": "Kendal","village":  "Sendang", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 4, "subvillage": "Ngejring", "village": "Sendang", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 5, "subvillage": "Kendal","village":  "Sendang", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 6, "subvillage": "Kendal","village":  "Sendang", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 7, "subvillage": "Kendal","village":  "Sendang", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 8, "subvillage": "Kendal", "village": "Sendang", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 9, "subvillage": "Sambi", "village": "Sendang", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 10, "subvillage":  "Kendal", "village": "Sendang", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 11, "subvillage":  "Sambi", "village": "Sendang", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 12, "subvillage":  "Sambi", "village": "Sendang", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 13, "subvillage":  "Petung", "village": "Kalak", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 14, "subvillage":  "Petung", "village": "Kalak", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 15, "subvillage":  "Bolo", "village": "Kalak", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 16, "subvillage":  "Bolo", "village": "Kalak", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 17, "subvillage":  "Ngobyogan", "village": "Kalak", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 18, "subvillage":  "Ngobyogan", "village": "Kalak", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"},
            {"tourist_attraction_id": 19, "subvillage":  "Ngobyogan", "village": "Kalak", "district": "Donorojo", "regency": "Pacitan", "province": "Jawa Timur"}
            ]
        )


def downgrade():
    op.execute("DELETE FROM address")
