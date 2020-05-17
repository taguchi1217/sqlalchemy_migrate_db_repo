#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(repository='.', url='postgresql+psycopg2://postgres:postgres@localhost/testdb2', debug='False')
