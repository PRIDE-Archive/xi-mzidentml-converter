from parser import MzIdParser
from parser.writer import Writer
from sqlalchemy import text
from uuid import uuid4
from .db_pytest_fixtures import *


def parse_mzid_into_postgresql(mzid_file, peaklist, tmpdir, logger, use_database, engine):  # remove 'use_database'? -cc
    # create temp user for user_id
    user_id = uuid4()
    with engine.connect() as conn:
        conn.execute(
            text(
                f"INSERT INTO UserAccount (id, user_name, password, email) VALUES "
                f"('{user_id}', 'testuser', 'testpw', 'testemail')"
            )
        )
    # create writer
    writer = Writer(engine.url, user_id)
    engine.dispose()

    # parse the mzid file
    id_parser = MzIdParser.MzIdParser(mzid_file, str(tmpdir), peaklist, writer, logger)
    id_parser.parse()
    return id_parser


def parse_mzid_into_sqlite_xispec(mzid_file, peaklist, tmpdir, logger, engine):
    # create writer
    writer = Writer(engine.url)
    engine.dispose()

    # parse the mzid file
    id_parser = MzIdParser.xiSPEC_MzIdParser(mzid_file, str(tmpdir), peaklist, writer, logger)
    id_parser.parse()
    return id_parser