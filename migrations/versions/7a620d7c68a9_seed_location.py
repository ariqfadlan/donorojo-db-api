"""seed location

Revision ID: 7a620d7c68a9
Revises: ef9349c42eaa
Create Date: 2021-08-12 13:17:06.427729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a620d7c68a9'
down_revision = 'ef9349c42eaa'
branch_labels = None
depends_on = None


location_table = sa.table('location',
        sa.column('tourist_attraction_id', sa.Integer),
        sa.column('latitude', sa.String),
        sa.column('longitude', sa.String)
    )
def upgrade():
    op.bulk_insert(location_table,
        [
            {"tourist_attraction_id": 1, "latitude": -8.2293562, "longitude": 110.958105},
            {"tourist_attraction_id": 2, "latitude": -8.226365, "longitude": 110.954433},
            {"tourist_attraction_id": 3, "latitude": -8.22479, "longitude": 110.939275},
            {"tourist_attraction_id": 4, "latitude": -8.187629, "longitude": 110.954458},
            {"tourist_attraction_id": 5, "latitude": -8.226802, "longitude": 110.940681},
            {"tourist_attraction_id": 6, "latitude": -8.2245022, "longitude": 110.9408755},
            {"tourist_attraction_id": 7, "latitude": -8.2247673, "longitude": 110.9452693},
            {"tourist_attraction_id": 8, "latitude": -8.225086, "longitude": 110.950386},
            {"tourist_attraction_id": 9, "latitude": -8.229294, "longitude": 110.960355},
            {"tourist_attraction_id": 10,"latitude":  -8.227047, "longitude": 110.940803},
            {"tourist_attraction_id": 11,"latitude":  -8.227969, "longitude": 110.956843},
            {"tourist_attraction_id": 12,"latitude":  -8.224971, "longitude": 110.951992},
            {"tourist_attraction_id": 13,"latitude":  -8.175843, "longitude": 110.9356253},
            {"tourist_attraction_id": 14,"latitude":  -8.167969, "longitude": 110.940685},
            {"tourist_attraction_id": 15,"latitude":  -8.218654, "longitude": 110.920055},
            {"tourist_attraction_id": 16,"latitude":  -8.219565, "longitude": 110.925031},
            {"tourist_attraction_id": 17,"latitude":  -8.221456, "longitude": 110.9310737},
            {"tourist_attraction_id": 18,"latitude":  -8.223411, "longitude": 110.937432},
            {"tourist_attraction_id": 19,"latitude":  -8.2216836, "longitude": 110.9332644}
            ]
        )


def downgrade():
    op.execute("DELETE FROM location")
