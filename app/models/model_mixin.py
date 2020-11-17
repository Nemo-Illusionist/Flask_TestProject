from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import expression
from sqlalchemy.types import DateTime


class UtcNow(expression.FunctionElement):
    type = DateTime()


# todo: put in class 'UtcNow'
@compiles(UtcNow, 'postgresql')
def pg_utc_now(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


class TimestampMixin(object):
    created_at = Column(DateTime, server_default=UtcNow(), nullable=False)
    updated_at = Column(DateTime, server_default=UtcNow(), server_onupdate=UtcNow(), nullable=False)


class DeleteMixin(object):
    delete_at = Column(DateTime, nullable=True)

    def set_deleted(self):
        # todo: set 'delete_at' in db, using class `UtcNow`
        self.delete_at = datetime.utcnow()
