title: sqlalchemy.ext compiler Example Code
category: page
slug: sqlalchemy-ext-compiler-examples
sortorder: 500031044
toc: False
sidebartitle: sqlalchemy.ext compiler
meta: Python example code that shows how to use the compiler callable from the sqlalchemy.ext module of the SQLAlchemy project.


`compiler` is a callable within the `sqlalchemy.ext` module of the SQLAlchemy project.



## Example 1 from Amazon Redshift SQLAlchemy Dialect
[Amazon Redshift SQLAlchemy Dialect](https://github.com/sqlalchemy-redshift/sqlalchemy-redshift)
is a [SQLAlchemy Dialect](https://docs.sqlalchemy.org/en/13/dialects/)
that can communicate with the [AWS Redshift](https://aws.amazon.com/redshift/)
data store. The SQL is essentially [PostgreSQL](/postgresql.html)
and requires [psycopg2](https://www.psycopg.org/) to properly
operate. This project and its code are open sourced under the
[MIT license](https://github.com/sqlalchemy-redshift/sqlalchemy-redshift/blob/master/LICENSE).

[**Amazon Redshift SQLAlchemy Dialect / sqlalchemy_redshift / commands.py**](https://github.com/sqlalchemy-redshift/sqlalchemy-redshift/blob/master/sqlalchemy_redshift/./commands.py)

```python
# commands.py
import enum
import numbers
import re
import warnings
try:
    from collections.abc import Iterable
except ImportError:
    from collections import Iterable

import sqlalchemy as sa
from sqlalchemy import exc as sa_exc
~~from sqlalchemy.ext import compiler as sa_compiler
from sqlalchemy.sql import expression as sa_expression



ACCESS_KEY_ID_RE = re.compile('[A-Z0-9]{20}')
SECRET_ACCESS_KEY_RE = re.compile('[A-Za-z0-9/+=]{40}')
TOKEN_RE = re.compile('[A-Za-z0-9/+=]+')
AWS_ACCOUNT_ID_RE = re.compile('[0-9]{12}')
IAM_ROLE_NAME_RE = re.compile('[A-Za-z0-9+=,.@-_]{1,64}')


def _process_aws_credentials(access_key_id=None, secret_access_key=None,
                             session_token=None, aws_account_id=None,
                             iam_role_name=None):

    if (access_key_id is not None and secret_access_key is not None and
            aws_account_id is not None and iam_role_name is not None):
        raise TypeError(
            'Either access key based credentials or role based credentials '
            'should be specified, but not both'
        )

    credentials = None



## ... source file abbreviated to get to compiler examples ...


        if ignore_extra and fill_target:
            raise ValueError(
                '"ignore_extra" cannot be used with "fill_target".')

        self.source = source
        self.target = target
        self.ignore_extra = ignore_extra
        self.fill_target = fill_target


@sa_compiler.compiles(AlterTableAppendCommand)
def visit_alter_table_append_command(element, compiler, **kw):
    if element.ignore_extra:
        fill_option = 'IGNOREEXTRA'
    elif element.fill_target:
        fill_option = 'FILLTARGET'
    else:
        fill_option = ''

    query_text = \
        'ALTER TABLE {target} APPEND FROM {source} {fill_option}'.format(
~~            target=compiler.preparer.format_table(element.target),
~~            source=compiler.preparer.format_table(element.source),
            fill_option=fill_option,
        )
~~    return compiler.process(sa.text(query_text), **kw)


class UnloadFromSelect(_ExecutableClause):

    def __init__(self, select, unload_location, access_key_id=None,
                 secret_access_key=None, session_token=None,
                 aws_account_id=None, iam_role_name=None,
                 manifest=False, delimiter=None, fixed_width=None,
                 encrypted=False, gzip=False, add_quotes=False, null=None,
                 escape=False, allow_overwrite=False, parallel=True,
                 header=False, region=None, max_file_size=None,
                 format=None):

        if delimiter is not None and len(delimiter) != 1:
            raise ValueError(
                '"delimiter" parameter must be a single character'
            )

        if header and fixed_width is not None:
            raise ValueError(
                "'header' cannot be used with 'fixed_width'"
            )

        credentials = _process_aws_credentials(


## ... source file abbreviated to get to compiler examples ...


    if element.max_error is not None:
        parameters.append('MAXERROR AS :error_count')
        bindparams.append(sa.bindparam(
            'error_count',
            value=element.max_error,
            type_=sa.Integer,
        ))

    if element.no_load:
        parameters.append('NOLOAD')

    if element.stat_update:
        parameters.append('STATUPDATE ON')
    elif element.stat_update is not None:
        parameters.append('STATUPDATE OFF')

    if element.region is not None:
        parameters.append('REGION :region')
        bindparams.append(sa.bindparam(
            'region',
            value=element.region,
            type_=sa.String
        ))

    columns = ' (%s)' % ', '.join(
~~        compiler.preparer.format_column(column) for column in element.columns
    ) if element.columns else ''

    qs = qs.format(
~~        table=compiler.preparer.format_table(element.table),
        columns=columns,
        format=format_,
        parameters='\n'.join(parameters)
    )

~~    return compiler.process(sa.text(qs).bindparams(*bindparams), **kw)


class CreateLibraryCommand(_ExecutableClause):
    def __init__(self, library_name, location, access_key_id=None,
                 secret_access_key=None, session_token=None,
                 aws_account_id=None, iam_role_name=None, replace=False,
                 region=None):
        self.library_name = library_name
        self.location = location
        self.credentials = _process_aws_credentials(
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
            session_token=session_token,
            aws_account_id=aws_account_id,
            iam_role_name=iam_role_name,
        )
        self.replace = replace
        self.region = region


@sa_compiler.compiles(CreateLibraryCommand)
def visit_create_library_command(element, compiler, **kw):
    query = """
        CREATE {or_replace} LIBRARY {name}


class AlterTableAppendCommand(_ExecutableClause):
    def __init__(self, source, target, ignore_extra=False, fill_target=False):


## ... source file continues with no further compiler examples...

```


## Example 2 from sqlalchemy-utils
[sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
([project documentation](https://sqlalchemy-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/SQLAlchemy-Utils/))
is a code library with various helper functions and new data types
that make it easier to use [SQLAlchemy](/sqlalchemy.html) when building
projects that involve more specific storage requirements such as
[currency](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.currency).
The wide array of
[data types](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html)
includes [ranged values](https://sqlalchemy-utils.readthedocs.io/en/latest/range_data_types.html)
and [aggregated attributes](https://sqlalchemy-utils.readthedocs.io/en/latest/aggregates.html).

[**sqlalchemy-utils / sqlalchemy_utils / view.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/./view.py)

```python
# view.py
import sqlalchemy as sa
~~from sqlalchemy.ext import compiler
from sqlalchemy.schema import DDLElement, PrimaryKeyConstraint


class CreateView(DDLElement):
    def __init__(self, name, selectable, materialized=False):
        self.name = name
        self.selectable = selectable
        self.materialized = materialized


@compiler.compiles(CreateView)
def compile_create_materialized_view(element, compiler, **kw):
    return 'CREATE {}VIEW {} AS {}'.format(
        'MATERIALIZED ' if element.materialized else '',
        element.name,
~~        compiler.sql_compiler.process(element.selectable, literal_binds=True),
    )


class DropView(DDLElement):
    def __init__(self, name, materialized=False, cascade=True):
        self.name = name
        self.materialized = materialized
        self.cascade = cascade


@compiler.compiles(DropView)
def compile_drop_materialized_view(element, compiler, **kw):
    return 'DROP {}VIEW IF EXISTS {} {}'.format(
        'MATERIALIZED ' if element.materialized else '',
        element.name,
        'CASCADE' if element.cascade else ''
    )


def create_table_from_selectable(
    name,
    selectable,
    indexes=None,
    metadata=None,


## ... source file continues with no further compiler examples...

```

