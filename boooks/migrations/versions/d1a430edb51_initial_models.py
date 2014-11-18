# flake8: noqa
"""initial models

Revision ID: d1a430edb51
Revises: None
Create Date: 2014-11-18 02:46:47.259927

"""

# revision identifiers, used by Alembic.
revision = 'd1a430edb51'
down_revision = None

from datetime import datetime
from alembic import op
import sqlalchemy as db




def DefaultForeignKey(field_name, parent_field_name,
                      ondelete='CASCADE', nullable=False, **kw):
    return db.Column(field_name, db.Integer,
                     db.ForeignKey(parent_field_name, ondelete=ondelete),
                     nullable=nullable, **kw)


def PrimaryKey(name='id'):
    return db.Column(name, db.Integer, primary_key=True)


def now():
    return datetime.now()


def upgrade():
    op.create_table(
        'book_author',
        PrimaryKey(),
        db.Column('name', db.Unicode(255)),
        db.Column('slug', db.Unicode(255)),
    )
    op.create_table(
        'book',
        PrimaryKey(),
        db.Column('ASIN', db.Unicode(20)),
        db.Column('ISBN', db.Unicode(20)),
        db.Column('title', db.Unicode(255)),
        db.Column('slug', db.Unicode(255)),
        db.Column('url', db.Unicode(255)),
        db.Column('number_of_pages', db.Integer),
        db.Column('price', db.Numeric),
        db.Column('stars', db.Integer),
        db.Column('ranking', db.Integer),
        db.Column('total_reviews', db.Integer),
        DefaultForeignKey('author_id', 'book_author.id')
    )




def downgrade():
    op.drop_table('book')
    op.drop_table('book_author')
