title: sqlalchemy.engine create_engine code examples
category: page
slug: sqlalchemy-engine-create-engine-examples
sortorder: 500031017
toc: False
sidebartitle: sqlalchemy.engine create_engine
meta: Python example code for the create_engine callable from the sqlalchemy.engine module of the SQLAlchemy project.


create_engine is a callable within the sqlalchemy.engine module of the SQLAlchemy project.


## Example 1 from sqlacodegen
[sqlacodegen](https://github.com/agronholm/sqlacodegen)
([PyPI package information](https://pypi.org/project/sqlacodegen/))
is a tool for
reading from an existing [relational database](/databases.html) to
generate code to create [SQLAlchemy](/sqlalchemy.html) models based
on that database. The project is primarily written and maintained
by [Alex Grönholm (agronholm)](https://github.com/agronholm) and it
is open sourced under the
[MIT license](https://github.com/agronholm/sqlacodegen/blob/master/LICENSE).

[**sqlacodegen / sqlacodegen / main.py**](https://github.com/agronholm/sqlacodegen/blob/master/sqlacodegen/./main.py)

```python
# main.py
from __future__ import unicode_literals, division, print_function, absolute_import

import argparse
import io
import sys

import pkg_resources
~~from sqlalchemy.engine import create_engine
from sqlalchemy.schema import MetaData

from sqlacodegen.codegen import CodeGenerator


def main():
    parser = argparse.ArgumentParser(
        description='Generates SQLAlchemy model code from an existing database.')
    parser.add_argument('url', nargs='?', help='SQLAlchemy url to the database')
    parser.add_argument('--version', action='store_true', help="print the version number and exit")
    parser.add_argument('--schema', help='load tables from an alternate schema')
    parser.add_argument('--tables', help='tables to process (comma-separated, default: all)')
    parser.add_argument('--noviews', action='store_true', help="ignore views")
    parser.add_argument('--noindexes', action='store_true', help='ignore indexes')
    parser.add_argument('--noconstraints', action='store_true', help='ignore constraints')
    parser.add_argument('--nojoined', action='store_true',
                        help="don't autodetect joined table inheritance")
    parser.add_argument('--noinflect', action='store_true',
                        help="don't try to convert tables names to singular form")
    parser.add_argument('--noclasses', action='store_true',
                        help="don't generate classes, only tables")
    parser.add_argument('--nocomments', action='store_true', help="don't render column comments")
    parser.add_argument('--outfile', help='file to write output to (default: stdout)')
    args = parser.parse_args()

    if args.version:
        version = pkg_resources.get_distribution('sqlacodegen').parsed_version
        print(version.public)
        return
    if not args.url:
        print('You must supply a url\n', file=sys.stderr)
        parser.print_help()
        return

~~    engine = create_engine(args.url)
    metadata = MetaData(engine)
    tables = args.tables.split(',') if args.tables else None
    metadata.reflect(engine, args.schema, not args.noviews, tables)

    outfile = io.open(args.outfile, 'w', encoding='utf-8') if args.outfile else sys.stdout
    generator = CodeGenerator(metadata, args.noindexes, args.noconstraints, args.nojoined,
                              args.noinflect, args.noclasses, nocomments=args.nocomments)
    generator.render(outfile)



## ... source file continues with no further create_engine examples...

```

