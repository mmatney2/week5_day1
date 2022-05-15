"""empty message

Revision ID: 25f126d45098
Revises: 
Create Date: 2022-05-15 16:21:29.170712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25f126d45098'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemen')
    op.add_column('pokeman', sa.Column('user_token', sa.String(), nullable=True))
    op.create_foreign_key(None, 'pokeman', 'user', ['user_token'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pokeman', type_='foreignkey')
    op.drop_column('pokeman', 'user_token')
    op.create_table('pokemen',
    sa.Column('poke_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user.id'], name='pokemen_id_fkey'),
    sa.ForeignKeyConstraint(['poke_id'], ['pokeman.poke_id'], name='pokemen_poke_id_fkey'),
    sa.PrimaryKeyConstraint('poke_id', 'id', name='pokemen_pkey')
    )
    # ### end Alembic commands ###
