#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""Add verify_ca column to cluster_template

Revision ID: dfe95f6712ac
Revises: bc46ba6cf949
Create Date: 2017-03-20 20:19:22.560466

"""

# revision identifiers, used by Alembic.
revision = 'dfe95f6712ac'
down_revision = 'bc46ba6cf949'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('cluster_template',
                  sa.Column('verify_ca', sa.Boolean(), default=True))
