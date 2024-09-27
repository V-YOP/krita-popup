
from pathlib import Path
from . import singleton
import sqlite3
from krita import *

@singleton
class ResourceDBHelper:
    """
    A Helper class for query resource info from krita db.

    **Only query is supported**, because krita will lock all tables while opening.
    """
    def __init__(self) -> None:
        resource_dir = Krita.instance().readSetting('', 'ResourceDirectory', 'WTF')
        # resource_dir = 'C:/Users/Administrator/AppData/Roaming/krita'
        assert resource_dir != 'WTF', 'WTF'
        self.conn = sqlite3.connect(Path(resource_dir)/'resourcecache.sqlite')

    def __execute_sql(self, sql: str):
        res = self.conn.execute(sql)
        return res.fetchall()

ResourceDBHelper()