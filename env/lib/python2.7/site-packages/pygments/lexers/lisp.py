# -*- coding: utf-8 -*-
"""
    pygments.lexers.lisp
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for Lispy languages.

    :copyright: Copyright 2006-2014 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, include, bygroups, words, default
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Literal, Error

from pygments.lexers.python import PythonLexer

__all__ = ['SchemeLexer', 'CommonLispLexer', 'HyLexer', 'RacketLexer',
           'NewLispLexer']


class SchemeLexer(RegexLexer):
    """
    A Scheme lexer, parsing a stream and outputting the tokens
    needed to highlight scheme code.
    This lexer could be most probably easily subclassed to parse
    other LISP-Dialects like Common Lisp, Emacs Lisp or AutoLisp.

    This parser is checked with pastes from the LISP pastebin
    at http://paste.lisp.org/ to cover as much syntax as possible.

    It supports the full Scheme syntax as defined in R5RS.

    .. versionadded:: 0.6
    """
    name = 'Scheme'
    aliases = ['scheme', 'scm']
    filenames = ['*.scm', '*.ss']
    mimetypes = ['text/x-scheme', 'application/x-scheme']

    # list of known keywords and builtins taken form vim 6.4 scheme.vim
    # syntax file.
    keywords = (
        'lambda', 'define', 'if', 'else', 'cond', 'and', 'or', 'case', 'let',
        'let*', 'letrec', 'begin', 'do', 'delay', 'set!', '=>', 'quote',
        'quasiquote', 'unquote', 'unquote-splicing', 'define-syntax',
        'let-syntax', 'letrec-syntax', 'syntax-rules'
    )
    builtins = (
        '*', '+', '-', '/', '<', '<=', '=', '>', '>=', 'abs', 'acos', 'angle',
        'append', 'apply', 'asin', 'assoc', 'assq', 'assv', 'atan',
        'boolean?', 'caaaar', 'caaadr', 'caaar', 'caadar', 'caaddr', 'caadr',
        'caar', 'cadaar', 'cadadr', 'cadar', 'caddar', 'cadddr', 'caddr',
        'cadr', 'call-with-current-continuation', 'call-with-input-file',
        'call-with-output-file', 'call-with-values', 'call/cc', 'car',
        'cdaaar', 'cdaadr', 'cdaar', 'cdadar', 'cdaddr', 'cdadr', 'cdar',
        'cddaar', 'cddadr', 'cddar', 'cdddar', 'cddddr', 'cdddr', 'cddr',
        'cdr', 'ceiling', 'char->integer', 'char-alphabetic?', 'char-ci<=?',
        'char-ci<?', 'char-ci=?', 'char-ci>=?', 'char-ci>?', 'char-downcase',
        'char-lower-case?', 'char-numeric?', 'char-ready?', 'char-upcase',
        'char-upper-case?', 'char-whitespace?', 'char<=?', 'char<?', 'char=?',
        'char>=?', 'char>?', 'char?', 'close-input-port', 'close-output-port',
        'complex?', 'cons', 'cos', 'current-input-port', 'current-output-port',
        'denominator', 'display', 'dynamic-wind', 'eof-object?', 'eq?',
        'equal?', 'eqv?', 'eval', 'even?', 'exact->inexact', 'exact?', 'exp',
        'expt', 'floor', 'for-each', 'force', 'gcd', 'imag-part',
        'inexact->exact', 'inexact?', 'input-port?', 'integer->char',
        'integer?', 'interaction-environment', 'lcm', 'length', 'list',
        'list->string', 'list->vector', 'list-ref', 'list-tail', 'list?',
        'load', 'log', 'magnitude', 'make-polar', 'make-rectangular',
        'make-string', 'make-vector', 'map', 'max', 'member', 'memq', 'memv',
        'min', 'modulo', 'negative?', 'newline', 'not', 'null-environment',
        'null?', 'number->string', 'number?', 'numerator', 'odd?',
        'open-input-file', 'open-output-file', 'output-port?', 'pair?',
        'peek-char', 'port?', 'positive?', 'procedure?', 'quotient',
        'rational?', 'rationalize', 'read', 'read-char', 'real-part', 'real?',
        'remainder', 'reverse', 'round', 'scheme-report-environment',
        'set-car!', 'set-cdr!', 'sin', 'sqrt', 'string', 'string->list',
        'string->number', 'string->symbol', 'string-append', 'string-ci<=?',
        'string-ci<?', 'string-ci=?', 'string-ci>=?', 'string-ci>?',
        'string-copy', 'string-fill!', 'string-length', 'string-ref',
        'string-set!', 'string<=?', 'string<?', 'string=?', 'string>=?',
        'string>?', 'string?', 'substring', 'symbol->string', 'symbol?',
        'tan', 'transcript-off', 'transcript-on', 'truncate', 'values',
        'vector', 'vector->list', 'vector-fill!', 'vector-length',
        'vector-ref', 'vector-set!', 'vector?', 'with-input-from-file',
        'with-output-to-file', 'write', 'write-char', 'zero?'
    )

    # valid names for identifiers
    # well, names can only not consist fully of numbers
    # but this should be good enough for now
    valid_name = r'[\w!$%&*+,/:<=>?@^~|-]+'

    tokens = {
        'root': [
            # the comments
            # and going to the end of the line
            (r';.*$', Comment.Single),
            # multi-line comment
            (r'#\|', Comment.Multiline, 'multiline-comment'),
            # commented form (entire sexpr folliwng)
            (r'#;\s*\(', Comment, 'commented-form'),
            # signifies that the program text that follows is written with the
            # lexical and datum syntax described in r6rs
            (r'#!r6rs', Comment),

            # whitespaces - usually not relevant
            (r'\s+', Text),

            # numbers
            (r'-?\d+\.\d+', Number.Float),
            (r'-?\d+', Number.Integer),
            # support for uncommon kinds of numbers -
            # have to figure out what the characters mean
            # (r'(#e|#i|#b|#o|#d|#x)[\d.]+', Number),

            # strings, symbols and characters
            (r'"(\\\\|\\"|[^"])*"', String),
            (r"'" + valid_name, String.Symbol),
            (r"#\\([()/'\"._!§$%& ?=+-]|[a-zA-Z0-9]+)", String.Char),

            # constants
            (r'(#t|#f)', Name.Constant),

            # special operators
            (r"('|#|`|,@|,|\.)", Operator),

            # highlight the keywords
            ('(%s)' % '|'.join(re.escape(entry) + ' ' for entry in keywords),
             Keyword),

            # first variable in a quoted string like
            # '(this is syntactic sugar)
            (r"(?<='\()" + valid_name, Name.Variable),
            (r"(?<=#\()" + valid_name, Name.Variable),

            # highlight the builtins
            ("(?<=\()(%s)" % '|'.join(re.escape(entry) + ' ' for entry in builtins),
             Name.Builtin),

            # the remaining functions
            (r'(?<=\()' + valid_name, Name.Function),
            # find the remaining variables
            (valid_name, Name.Variable),

            # the famous parentheses!
            (r'(\(|\))', Punctuation),
            (r'(\[|\])', Punctuation),
        ],
        'multiline-comment': [
            (r'#\|', Comment.Multiline, '#push'),
            (r'\|#', Comment.Multiline, '#pop'),
            (r'[^|#]+', Comment.Multiline),
            (r'[|#]', Comment.Multiline),
        ],
        'commented-form': [
            (r'\(', Comment, '#push'),
            (r'\)', Comment, '#pop'),
            (r'[^()]+', Comment),
        ],
    }


class CommonLispLexer(RegexLexer):
    """
    A Common Lisp lexer.

    .. versionadded:: 0.9
    """
    name = 'Common Lisp'
    aliases = ['common-lisp', 'cl', 'lisp', 'elisp', 'emacs', 'emacs-lisp']
    filenames = ['*.cl', '*.lisp', '*.el']  # use for Elisp too
    mimetypes = ['text/x-common-lisp']

    flags = re.IGNORECASE | re.MULTILINE

    # couple of useful regexes

    # characters that are not macro-characters and can be used to begin a symbol
    nonmacro = r'\\.|[\w!$%&*+-/<=>?@\[\]^{}~]'
    constituent = nonmacro + '|[#.:]'
    terminated = r'(?=[ "()\'\n,;`])'  # whitespace or terminating macro characters

    # symbol token, reverse-engineered from hyperspec
    # Take a deep breath...
    symbol = r'(\|[^|]+\||(?:%s)(?:%s)*)' % (nonmacro, constituent)

    def __init__(self, **options):
        from pygments.lexers._cl_builtins import BUILTIN_FUNCTIONS, \
            SPECIAL_FORMS, MACROS, LAMBDA_LIST_KEYWORDS, DECLARATIONS, \
            BUILTIN_TYPES, BUILTIN_CLASSES
        self.builtin_function = BUILTIN_FUNCTIONS
        self.special_forms = SPECIAL_FORMS
        self.macros = MACROS
        self.lambda_list_keywords = LAMBDA_LIST_KEYWORDS
        self.declarations = DECLARATIONS
        self.builtin_types = BUILTIN_TYPES
        self.builtin_classes = BUILTIN_CLASSES
        RegexLexer.__init__(self, **options)

    def get_tokens_unprocessed(self, text):
        stack = ['root']
        for index, token, value in RegexLexer.get_tokens_unprocessed(self, text, stack):
            if token is Name.Variable:
                if value in self.builtin_function:
                    yield index, Name.Builtin, value
                    continue
                if value in self.special_forms:
                    yield index, Keyword, value
                    continue
                if value in self.macros:
                    yield index, Name.Builtin, value
                    continue
                if value in self.lambda_list_keywords:
                    yield index, Keyword, value
                    continue
                if value in self.declarations:
                    yield index, Keyword, value
                    continue
                if value in self.builtin_types:
                    yield index, Keyword.Type, value
                    continue
                if value in self.builtin_classes:
                    yield index, Name.Class, value
                    continue
            yield index, token, value

    tokens = {
        'root': [
            default('body'),
        ],
        'multiline-comment': [
            (r'#\|', Comment.Multiline, '#push'),  # (cf. Hyperspec 2.4.8.19)
            (r'\|#', Comment.Multiline, '#pop'),
            (r'[^|#]+', Comment.Multiline),
            (r'[|#]', Comment.Multiline),
        ],
        'commented-form': [
            (r'\(', Comment.Preproc, '#push'),
            (r'\)', Comment.Preproc, '#pop'),
            (r'[^()]+', Comment.Preproc),
        ],
        'body': [
            # whitespace
            (r'\s+', Text),

            # single-line comment
            (r';.*$', Comment.Single),

            # multi-line comment
            (r'#\|', Comment.Multiline, 'multiline-comment'),

            # encoding comment (?)
            (r'#\d*Y.*$', Comment.Special),

            # strings and characters
            (r'"(\\.|\\\n|[^"\\])*"', String),
            # quoting
            (r":" + symbol, String.Symbol),
            (r"::" + symbol, String.Symbol),
            (r":#" + symbol, String.Symbol),
            (r"'" + symbol, String.Symbol),
            (r"'", Operator),
            (r"`", Operator),

            # decimal numbers
            (r'[-+]?\d+\.?' + terminated, Number.Integer),
            (r'[-+]?\d+/\d+' + terminated, Number),
            (r'[-+]?(\d*\.\d+([defls][-+]?\d+)?|\d+(\.\d*)?[defls][-+]?\d+)'
                + terminated, Number.Float),

            # sharpsign strings and characters
            (r"#\\." + terminated, String.Char),
            (r"#\\" + symbol, String.Char),

            # vector
            (r'#\(', Operator, 'body'),

            # bitstring
            (r'#\d*\*[01]*', Literal.Other),

            # uninterned symbol
            (r'#:' + symbol, String.Symbol),

            # read-time and load-time evaluation
            (r'#[.,]', Operator),

            # function shorthand
            (r'#\'', Name.Function),

            # binary rational
            (r'#b[+-]?[01]+(/[01]+)?', Number.Bin),

            # octal rational
            (r'#o[+-]?[0-7]+(/[0-7]+)?', Number.Oct),

            # hex rational
            (r'#x[+-]?[0-9a-f]+(/[0-9a-f]+)?', Number.Hex),

            # radix rational
            (r'#\d+r[+-]?[0-9a-z]+(/[0-9a-z]+)?', Number),

            # complex
            (r'(#c)(\()', bygroups(Number, Punctuation), 'body'),

            # array
            (r'(#\d+a)(\()', bygroups(Literal.Other, Punctuation), 'body'),

            # structure
            (r'(#s)(\()', bygroups(Literal.Other, Punctuation), 'body'),

            # path
            (r'#p?"(\\.|[^"])*"', Literal.Other),

            # reference
            (r'#\d+=', Operator),
            (r'#\d+#', Operator),

            # read-time comment
            (r'#+nil' + terminated + '\s*\(', Comment.Preproc, 'commented-form'),

            # read-time conditional
            (r'#[+-]', Operator),

            # special operators that should have been parsed already
            (r'(,@|,|\.)', Operator),

            # special constants
            (r'(t|nil)' + terminated, Name.Constant),

            # functions and variables
            (r'\*' + symbol + '\*', Name.Variable.Global),
            (symbol, Name.Variable),

            # parentheses
            (r'\(', Punctuation, 'body'),
            (r'\)', Punctuation, '#pop'),
        ],
    }


class HyLexer(RegexLexer):
    """
    Lexer for `Hy <http://hylang.org/>`_ source code.

    .. versionadded:: 2.0
    """
    name = 'Hy'
    aliases = ['hylang']
    filenames = ['*.hy']
    mimetypes = ['text/x-hy', 'application/x-hy']

    special_forms = (
        'cond', 'for', '->', '->>', 'car',
        'cdr', 'first', 'rest', 'let', 'when', 'unless',
        'import', 'do', 'progn', 'get', 'slice', 'assoc', 'with-decorator',
        ',', 'list_comp', 'kwapply', '~', 'is', 'in', 'is-not', 'not-in',
        'quasiquote', 'unquote', 'unquote-splice', 'quote', '|', '<<=', '>>=',
        'foreach', 'while',
        'eval-and-compile', 'eval-when-compile'
    )

    declarations = (
        'def', 'defn', 'defun', 'defmacro', 'defclass', 'lambda', 'fn', 'setv'
    )

    hy_builtins = ()

    hy_core = (
        'cycle', 'dec', 'distinct', 'drop', 'even?', 'filter', 'inc',
        'instance?', 'iterable?', 'iterate', 'iterator?', 'neg?',
        'none?', 'nth', 'numeric?', 'odd?', 'pos?', 'remove', 'repeat',
        'repeatedly', 'take', 'take_nth', 'take_while', 'zero?'
    )

    builtins = hy_builtins + hy_core

    # valid names for identifiers
    # well, names can only not consist fully of numbers
    # but this should be good enough for now
    valid_name = r'(?!#)[\w!$%*+<=>?/.#-]+'

    def _multi_escape(entries):
        return words(entries, suffix=' ')

    tokens = {
        'root': [
            # the comments - always starting with semicolon
            # and going to the end of the line
            (r';.*$', Comment.Single),

            # whitespaces - usually not relevant
            (r'[,\s]+', Text),

            # numbers
            (r'-?\d+\.\d+', Number.Float),
            (r'-?\d+', Number.Integer),
            (r'0[0-7]+j?', Number.Oct),
            (r'0[xX][a-fA-F0-9]+', Number.Hex),

            # strings, symbols and characters
            (r'"(\\\\|\\"|[^"])*"', String),
            (r"'" + valid_name, String.Symbol),
            (r"\\(.|[a-z]+)", String.Char),
            (r'^(\s*)([rRuU]{,2}"""(?:.|\n)*?""")', bygroups(Text, String.Doc)),
            (r"^(\s*)([rRuU]{,2}'''(?:.|\n)*?''')", bygroups(Text, String.Doc)),

            # keywords
            (r'::?' + valid_name, String.Symbol),

            # special operators
            (r'~@|[`\'#^~&@]', Operator),

            include('py-keywords'),
            include('py-builtins'),

            # highlight the special forms
            (_multi_escape(special_forms), Keyword),

            # Technically, only the special forms are 'keywords'. The problem
            # is that only treating them as keywords means that things like
            # 'defn' and 'ns' need to be highlighted as builtins. This is ugly
            # and weird for most styles. So, as a compromise we're going to
            # highlight them as Keyword.Declarations.
            (_multi_escape(declarations), Keyword.Declaration),

            # highlight the builtins
            (_multi_escape(builtins), Name.Builtin),

            # the remaining functions
            (r'(?<=\()' + valid_name, Name.Function),

            # find the remaining variables
            (valid_name, Name.Variable),

            # Hy accepts vector notation
            (r'(\[|\])', Punctuation),

            # Hy accepts map notation
            (r'(\{|\})', Punctuation),

            # the famous parentheses!
            (r'(\(|\))', Punctuation),

        ],
        'py-keywords': PythonLexer.tokens['keywords'],
        'py-builtins': PythonLexer.tokens['builtins'],
    }

    def analyse_text(text):
        if '(import ' in text or '(defn ' in text:
            return 0.9


class RacketLexer(RegexLexer):
    """
    Lexer for `Racket <http://racket-lang.org/>`_ source code (formerly
    known as PLT Scheme).

    .. versionadded:: 1.6
    """

    name = 'Racket'
    aliases = ['racket', 'rkt']
    filenames = ['*.rkt', '*.rktd', '*.rktl']
    mimetypes = ['text/x-racket', 'application/x-racket']

    # Generated by example.rkt
    _keywords = (
        '#%app', '#%datum', '#%declare', '#%expression', '#%module-begin',
        '#%plain-app', '#%plain-lambda', '#%plain-module-begin',
        '#%printing-module-begin', '#%provide', '#%require',
        '#%stratified-body', '#%top', '#%top-interaction',
        '#%variable-reference', '->', '->*', '->*m', '->d', '->dm', '->i',
        '->m', '...', ':do-in', '==', '=>', '_', 'absent', 'abstract',
        'all-defined-out', 'all-from-out', 'and', 'any', 'augment', 'augment*',
        'augment-final', 'augment-final*', 'augride', 'augride*', 'begin',
        'begin-for-syntax', 'begin0', 'case', 'case->', 'case->m',
        'case-lambda', 'class', 'class*', 'class-field-accessor',
        'class-field-mutator', 'class/c', 'class/derived', 'combine-in',
        'combine-out', 'command-line', 'compound-unit', 'compound-unit/infer',
        'cond', 'contract', 'contract-out', 'contract-struct', 'contracted',
        'define', 'define-compound-unit', 'define-compound-unit/infer',
        'define-contract-struct', 'define-custom-hash-types',
        'define-custom-set-types', 'define-for-syntax',
        'define-local-member-name', 'define-logger', 'define-match-expander',
        'define-member-name', 'define-module-boundary-contract',
        'define-namespace-anchor', 'define-opt/c', 'define-sequence-syntax',
        'define-serializable-class', 'define-serializable-class*',
        'define-signature', 'define-signature-form', 'define-struct',
        'define-struct/contract', 'define-struct/derived', 'define-syntax',
        'define-syntax-rule', 'define-syntaxes', 'define-unit',
        'define-unit-binding', 'define-unit-from-context',
        'define-unit/contract', 'define-unit/new-import-export',
        'define-unit/s', 'define-values', 'define-values-for-export',
        'define-values-for-syntax', 'define-values/invoke-unit',
        'define-values/invoke-unit/infer', 'define/augment',
        'define/augment-final', 'define/augride', 'define/contract',
        'define/final-prop', 'define/match', 'define/overment',
        'define/override', 'define/override-final', 'define/private',
        'define/public', 'define/public-final', 'define/pubment',
        'define/subexpression-pos-prop', 'delay', 'delay/idle', 'delay/name',
        'delay/strict', 'delay/sync', 'delay/thread', 'do', 'else', 'except',
        'except-in', 'except-out', 'export', 'extends', 'failure-cont',
        'false', 'false/c', 'field', 'field-bound?', 'file',
        'flat-murec-contract', 'flat-rec-contract', 'for', 'for*', 'for*/and',
        'for*/first', 'for*/fold', 'for*/fold/derived', 'for*/hash',
        'for*/hasheq', 'for*/hasheqv', 'for*/last', 'for*/list', 'for*/lists',
        'for*/mutable-set', 'for*/mutable-seteq', 'for*/mutable-seteqv',
        'for*/or', 'for*/product', 'for*/set', 'for*/seteq', 'for*/seteqv',
        'for*/sum', 'for*/vector', 'for*/weak-set', 'for*/weak-seteq',
        'for*/weak-seteqv', 'for-label', 'for-meta', 'for-syntax',
        'for-template', 'for/and', 'for/first', 'for/fold', 'for/fold/derived',
        'for/hash', 'for/hasheq', 'for/hasheqv', 'for/last', 'for/list',
        'for/lists', 'for/mutable-set', 'for/mutable-seteq',
        'for/mutable-seteqv', 'for/or', 'for/product', 'for/set', 'for/seteq',
        'for/seteqv', 'for/sum', 'for/vector', 'for/weak-set',
        'for/weak-seteq', 'for/weak-seteqv', 'gen:custom-write', 'gen:dict',
        'gen:equal+hash', 'gen:set', 'gen:stream', 'generic', 'get-field',
        'if', 'implies', 'import', 'include', 'include-at/relative-to',
        'include-at/relative-to/reader', 'include/reader', 'inherit',
        'inherit-field', 'inherit/inner', 'inherit/super', 'init',
        'init-depend', 'init-field', 'init-rest', 'inner', 'inspect',
        'instantiate', 'interface', 'interface*', 'invoke-unit',
        'invoke-unit/infer', 'lambda', 'lazy', 'let', 'let*', 'let*-values',
        'let-syntax', 'let-syntaxes', 'let-values', 'let/cc', 'let/ec',
        'letrec', 'letrec-syntax', 'letrec-syntaxes', 'letrec-syntaxes+values',
        'letrec-values', 'lib', 'link', 'local', 'local-require', 'log-debug',
        'log-error', 'log-fatal', 'log-info', 'log-warning', 'match', 'match*',
        'match*/derived', 'match-define', 'match-define-values',
        'match-lambda', 'match-lambda*', 'match-lambda**', 'match-let',
        'match-let*', 'match-let*-values', 'match-let-values', 'match-letrec',
        'match/derived', 'match/values', 'member-name-key', 'method-contract?',
        'mixin', 'module', 'module*', 'module+', 'nand', 'new', 'nor',
        'object-contract', 'object/c', 'only', 'only-in', 'only-meta-in',
        'open', 'opt/c', 'or', 'overment', 'overment*', 'override',
        'override*', 'override-final', 'override-final*', 'parameterize',
        'parameterize*', 'parameterize-break', 'parametric->/c', 'place',
        'place*', 'planet', 'prefix', 'prefix-in', 'prefix-out', 'private',
        'private*', 'prompt-tag/c', 'protect-out', 'provide',
        'provide-signature-elements', 'provide/contract', 'public', 'public*',
        'public-final', 'public-final*', 'pubment', 'pubment*', 'quasiquote',
        'quasisyntax', 'quasisyntax/loc', 'quote', 'quote-syntax',
        'quote-syntax/prune', 'recontract-out', 'recursive-contract',
        'relative-in', 'rename', 'rename-in', 'rename-inner', 'rename-out',
        'rename-super', 'require', 'send', 'send*', 'send+', 'send-generic',
        'send/apply', 'send/keyword-apply', 'set!', 'set!-values',
        'set-field!', 'shared', 'stream', 'stream-cons', 'struct', 'struct*',
        'struct-copy', 'struct-field-index', 'struct-out', 'struct/c',
        'struct/ctc', 'struct/dc', 'submod', 'super', 'super-instantiate',
        'super-make-object', 'super-new', 'syntax', 'syntax-case',
        'syntax-case*', 'syntax-id-rules', 'syntax-rules', 'syntax/loc', 'tag',
        'this', 'this%', 'thunk', 'thunk*', 'time', 'unconstrained-domain->',
        'unit', 'unit-from-context', 'unit/c', 'unit/new-import-export',
        'unit/s', 'unless', 'unquote', 'unquote-splicing', 'unsyntax',
        'unsyntax-splicing', 'values/drop', 'when', 'with-continuation-mark',
        'with-contract', 'with-handlers', 'with-handlers*', 'with-method',
        'with-syntax', u'λ'
    )

    # Generated by example.rkt
    _builtins = (
        '*', '+', '-', '/', '<', '</c', '<=', '<=/c', '=', '=/c', '>', '>/c',
        '>=', '>=/c', 'abort-current-continuation', 'abs', 'absolute-path?',
        'acos', 'add-between', 'add1', 'alarm-evt', 'always-evt', 'and/c',
        'andmap', 'angle', 'any/c', 'append', 'append*', 'append-map', 'apply',
        'argmax', 'argmin', 'arithmetic-shift', 'arity-at-least',
        'arity-at-least-value', 'arity-at-least?', 'arity-checking-wrapper',
        'arity-includes?', 'arity=?', 'asin', 'assf', 'assoc', 'assq', 'assv',
        'atan', 'bad-number-of-results', 'banner', 'base->-doms/c',
        'base->-rngs/c', 'base->?', 'between/c', 'bitwise-and',
        'bitwise-bit-field', 'bitwise-bit-set?', 'bitwise-ior', 'bitwise-not',
        'bitwise-xor', 'blame-add-car-context', 'blame-add-cdr-context',
        'blame-add-context', 'blame-add-missing-party',
        'blame-add-nth-arg-context', 'blame-add-or-context',
        'blame-add-range-context', 'blame-add-unknown-context',
        'blame-context', 'blame-contract', 'blame-fmt->-string',
        'blame-negative', 'blame-original?', 'blame-positive',
        'blame-replace-negative', 'blame-source', 'blame-swap',
        'blame-swapped?', 'blame-update', 'blame-value', 'blame?', 'boolean=?',
        'boolean?', 'bound-identifier=?', 'box', 'box-cas!', 'box-immutable',
        'box-immutable/c', 'box/c', 'box?', 'break-enabled', 'break-thread',
        'build-chaperone-contract-property', 'build-compound-type-name',
        'build-contract-property', 'build-flat-contract-property',
        'build-list', 'build-path', 'build-path/convention-type',
        'build-string', 'build-vector', 'byte-pregexp', 'byte-pregexp?',
        'byte-ready?', 'byte-regexp', 'byte-regexp?', 'byte?', 'bytes',
        'bytes->immutable-bytes', 'bytes->list', 'bytes->path',
        'bytes->path-element', 'bytes->string/latin-1', 'bytes->string/locale',
        'bytes->string/utf-8', 'bytes-append', 'bytes-append*',
        'bytes-close-converter', 'bytes-convert', 'bytes-convert-end',
        'bytes-converter?', 'bytes-copy', 'bytes-copy!',
        'bytes-environment-variable-name?', 'bytes-fill!', 'bytes-join',
        'bytes-length', 'bytes-no-nuls?', 'bytes-open-converter', 'bytes-ref',
        'bytes-set!', 'bytes-utf-8-index', 'bytes-utf-8-length',
        'bytes-utf-8-ref', 'bytes<?', 'bytes=?', 'bytes>?', 'bytes?', 'caaaar',
        'caaadr', 'caaar', 'caadar', 'caaddr', 'caadr', 'caar', 'cadaar',
        'cadadr', 'cadar', 'caddar', 'cadddr', 'caddr', 'cadr',
        'call-in-nested-thread', 'call-with-atomic-output-file',
        'call-with-break-parameterization',
        'call-with-composable-continuation', 'call-with-continuation-barrier',
        'call-with-continuation-prompt', 'call-with-current-continuation',
        'call-with-default-reading-parameterization',
        'call-with-escape-continuation', 'call-with-exception-handler',
        'call-with-file-lock/timeout', 'call-with-immediate-continuation-mark',
        'call-with-input-bytes', 'call-with-input-file',
        'call-with-input-file*', 'call-with-input-string',
        'call-with-output-bytes', 'call-with-output-file',
        'call-with-output-file*', 'call-with-output-string',
        'call-with-parameterization', 'call-with-semaphore',
        'call-with-semaphore/enable-break', 'call-with-values', 'call/cc',
        'call/ec', 'car', 'cdaaar', 'cdaadr', 'cdaar', 'cdadar', 'cdaddr',
        'cdadr', 'cdar', 'cddaar', 'cddadr', 'cddar', 'cdddar', 'cddddr',
        'cdddr', 'cddr', 'cdr', 'ceiling', 'channel-get', 'channel-put',
        'channel-put-evt', 'channel-put-evt?', 'channel-try-get', 'channel/c',
        'channel?', 'chaperone-box', 'chaperone-channel',
        'chaperone-continuation-mark-key', 'chaperone-contract-property?',
        'chaperone-contract?', 'chaperone-evt', 'chaperone-hash',
        'chaperone-of?', 'chaperone-procedure', 'chaperone-prompt-tag',
        'chaperone-struct', 'chaperone-struct-type', 'chaperone-vector',
        'chaperone?', 'char->integer', 'char-alphabetic?', 'char-blank?',
        'char-ci<=?', 'char-ci<?', 'char-ci=?', 'char-ci>=?', 'char-ci>?',
        'char-downcase', 'char-foldcase', 'char-general-category',
        'char-graphic?', 'char-iso-control?', 'char-lower-case?',
        'char-numeric?', 'char-punctuation?', 'char-ready?', 'char-symbolic?',
        'char-title-case?', 'char-titlecase', 'char-upcase',
        'char-upper-case?', 'char-utf-8-length', 'char-whitespace?', 'char<=?',
        'char<?', 'char=?', 'char>=?', 'char>?', 'char?',
        'check-duplicate-identifier', 'checked-procedure-check-and-extract',
        'choice-evt', 'class->interface', 'class-info', 'class?',
        'cleanse-path', 'close-input-port', 'close-output-port',
        'coerce-chaperone-contract', 'coerce-chaperone-contracts',
        'coerce-contract', 'coerce-contract/f', 'coerce-contracts',
        'coerce-flat-contract', 'coerce-flat-contracts', 'collect-garbage',
        'collection-file-path', 'collection-path', 'compile',
        'compile-allow-set!-undefined', 'compile-context-preservation-enabled',
        'compile-enforce-module-constants', 'compile-syntax',
        'compiled-expression?', 'compiled-module-expression?',
        'complete-path?', 'complex?', 'compose', 'compose1', 'conjugate',
        'cons', 'cons/c', 'cons?', 'const', 'continuation-mark-key/c',
        'continuation-mark-key?', 'continuation-mark-set->context',
        'continuation-mark-set->list', 'continuation-mark-set->list*',
        'continuation-mark-set-first', 'continuation-mark-set?',
        'continuation-marks', 'continuation-prompt-available?',
        'continuation-prompt-tag?', 'continuation?',
        'contract-continuation-mark-key', 'contract-first-order',
        'contract-first-order-passes?', 'contract-name', 'contract-proc',
        'contract-projection', 'contract-property?',
        'contract-random-generate', 'contract-stronger?',
        'contract-struct-exercise', 'contract-struct-generate',
        'contract-val-first-projection', 'contract?', 'convert-stream',
        'copy-directory/files', 'copy-file', 'copy-port', 'cos', 'cosh',
        'count', 'current-blame-format', 'current-break-parameterization',
        'current-code-inspector', 'current-command-line-arguments',
        'current-compile', 'current-compiled-file-roots',
        'current-continuation-marks', 'current-contract-region',
        'current-custodian', 'current-directory', 'current-directory-for-user',
        'current-drive', 'current-environment-variables', 'current-error-port',
        'current-eval', 'current-evt-pseudo-random-generator',
        'current-future', 'current-gc-milliseconds',
        'current-get-interaction-input-port', 'current-inexact-milliseconds',
        'current-input-port', 'current-inspector',
        'current-library-collection-links', 'current-library-collection-paths',
        'current-load', 'current-load-extension',
        'current-load-relative-directory', 'current-load/use-compiled',
        'current-locale', 'current-logger', 'current-memory-use',
        'current-milliseconds', 'current-module-declare-name',
        'current-module-declare-source', 'current-module-name-resolver',
        'current-module-path-for-load', 'current-namespace',
        'current-output-port', 'current-parameterization',
        'current-preserved-thread-cell-values', 'current-print',
        'current-process-milliseconds', 'current-prompt-read',
        'current-pseudo-random-generator', 'current-read-interaction',
        'current-reader-guard', 'current-readtable', 'current-seconds',
        'current-security-guard', 'current-subprocess-custodian-mode',
        'current-thread', 'current-thread-group',
        'current-thread-initial-stack-size',
        'current-write-relative-directory', 'curry', 'curryr',
        'custodian-box-value', 'custodian-box?', 'custodian-limit-memory',
        'custodian-managed-list', 'custodian-memory-accounting-available?',
        'custodian-require-memory', 'custodian-shutdown-all', 'custodian?',
        'custom-print-quotable-accessor', 'custom-print-quotable?',
        'custom-write-accessor', 'custom-write-property-proc', 'custom-write?',
        'date', 'date*', 'date*-nanosecond', 'date*-time-zone-name', 'date*?',
        'date-day', 'date-dst?', 'date-hour', 'date-minute', 'date-month',
        'date-second', 'date-time-zone-offset', 'date-week-day', 'date-year',
        'date-year-day', 'date?', 'datum->syntax', 'datum-intern-literal',
        'default-continuation-prompt-tag', 'degrees->radians',
        'delete-directory', 'delete-directory/files', 'delete-file',
        'denominator', 'dict->list', 'dict-can-functional-set?',
        'dict-can-remove-keys?', 'dict-clear', 'dict-clear!', 'dict-copy',
        'dict-count', 'dict-empty?', 'dict-for-each', 'dict-has-key?',
        'dict-implements/c', 'dict-implements?', 'dict-iter-contract',
        'dict-iterate-first', 'dict-iterate-key', 'dict-iterate-next',
        'dict-iterate-value', 'dict-key-contract', 'dict-keys', 'dict-map',
        'dict-mutable?', 'dict-ref', 'dict-ref!', 'dict-remove',
        'dict-remove!', 'dict-set', 'dict-set!', 'dict-set*', 'dict-set*!',
        'dict-update', 'dict-update!', 'dict-value-contract', 'dict-values',
        'dict?', 'directory-exists?', 'directory-list', 'display',
        'display-lines', 'display-lines-to-file', 'display-to-file',
        'displayln', 'double-flonum?', 'drop', 'drop-right', 'dropf',
        'dropf-right', 'dump-memory-stats', 'dup-input-port',
        'dup-output-port', 'dynamic-get-field', 'dynamic-place',
        'dynamic-place*', 'dynamic-require', 'dynamic-require-for-syntax',
        'dynamic-send', 'dynamic-set-field!', 'dynamic-wind', 'eighth',
        'empty', 'empty-sequence', 'empty-stream', 'empty?',
        'environment-variables-copy', 'environment-variables-names',
        'environment-variables-ref', 'environment-variables-set!',
        'environment-variables?', 'eof', 'eof-evt', 'eof-object?',
        'ephemeron-value', 'ephemeron?', 'eprintf', 'eq-contract-val',
        'eq-contract?', 'eq-hash-code', 'eq?', 'equal-contract-val',
        'equal-contract?', 'equal-hash-code', 'equal-secondary-hash-code',
        'equal<%>', 'equal?', 'equal?/recur', 'eqv-hash-code', 'eqv?', 'error',
        'error-display-handler', 'error-escape-handler',
        'error-print-context-length', 'error-print-source-location',
        'error-print-width', 'error-value->string-handler', 'eval',
        'eval-jit-enabled', 'eval-syntax', 'even?', 'evt/c', 'evt?',
        'exact->inexact', 'exact-ceiling', 'exact-floor', 'exact-integer?',
        'exact-nonnegative-integer?', 'exact-positive-integer?', 'exact-round',
        'exact-truncate', 'exact?', 'executable-yield-handler', 'exit',
        'exit-handler', 'exn', 'exn-continuation-marks', 'exn-message',
        'exn:break', 'exn:break-continuation', 'exn:break:hang-up',
        'exn:break:hang-up?', 'exn:break:terminate', 'exn:break:terminate?',
        'exn:break?', 'exn:fail', 'exn:fail:contract',
        'exn:fail:contract:arity', 'exn:fail:contract:arity?',
        'exn:fail:contract:blame', 'exn:fail:contract:blame-object',
        'exn:fail:contract:blame?', 'exn:fail:contract:continuation',
        'exn:fail:contract:continuation?', 'exn:fail:contract:divide-by-zero',
        'exn:fail:contract:divide-by-zero?',
        'exn:fail:contract:non-fixnum-result',
        'exn:fail:contract:non-fixnum-result?', 'exn:fail:contract:variable',
        'exn:fail:contract:variable-id', 'exn:fail:contract:variable?',
        'exn:fail:contract?', 'exn:fail:filesystem',
        'exn:fail:filesystem:errno', 'exn:fail:filesystem:errno-errno',
        'exn:fail:filesystem:errno?', 'exn:fail:filesystem:exists',
        'exn:fail:filesystem:exists?', 'exn:fail:filesystem:missing-module',
        'exn:fail:filesystem:missing-module-path',
        'exn:fail:filesystem:missing-module?', 'exn:fail:filesystem:version',
        'exn:fail:filesystem:version?', 'exn:fail:filesystem?',
        'exn:fail:network', 'exn:fail:network:errno',
        'exn:fail:network:errno-errno', 'exn:fail:network:errno?',
        'exn:fail:network?', 'exn:fail:object', 'exn:fail:object?',
        'exn:fail:out-of-memory', 'exn:fail:out-of-memory?', 'exn:fail:read',
        'exn:fail:read-srclocs', 'exn:fail:read:eof', 'exn:fail:read:eof?',
        'exn:fail:read:non-char', 'exn:fail:read:non-char?', 'exn:fail:read?',
        'exn:fail:syntax', 'exn:fail:syntax-exprs',
        'exn:fail:syntax:missing-module',
        'exn:fail:syntax:missing-module-path',
        'exn:fail:syntax:missing-module?', 'exn:fail:syntax:unbound',
        'exn:fail:syntax:unbound?', 'exn:fail:syntax?', 'exn:fail:unsupported',
        'exn:fail:unsupported?', 'exn:fail:user', 'exn:fail:user?',
        'exn:fail?', 'exn:misc:match?', 'exn:missing-module-accessor',
        'exn:missing-module?', 'exn:srclocs-accessor', 'exn:srclocs?', 'exn?',
        'exp', 'expand', 'expand-once', 'expand-syntax', 'expand-syntax-once',
        'expand-syntax-to-top-form', 'expand-to-top-form', 'expand-user-path',
        'explode-path', 'expt', 'externalizable<%>', 'false?', 'field-names',
        'fifth', 'file->bytes', 'file->bytes-lines', 'file->lines',
        'file->list', 'file->string', 'file->value', 'file-exists?',
        'file-name-from-path', 'file-or-directory-identity',
        'file-or-directory-modify-seconds', 'file-or-directory-permissions',
        'file-position', 'file-position*', 'file-size',
        'file-stream-buffer-mode', 'file-stream-port?', 'file-truncate',
        'filename-extension', 'filesystem-change-evt',
        'filesystem-change-evt-cancel', 'filesystem-change-evt?',
        'filesystem-root-list', 'filter', 'filter-map', 'filter-not',
        'filter-read-input-port', 'find-executable-path', 'find-files',
        'find-library-collection-links', 'find-library-collection-paths',
        'find-relative-path', 'find-system-path', 'findf', 'first', 'fixnum?',
        'flat-contract', 'flat-contract-predicate', 'flat-contract-property?',
        'flat-contract?', 'flat-named-contract', 'flatten',
        'floating-point-bytes->real', 'flonum?', 'floor', 'flush-output',
        'fold-files', 'foldl', 'foldr', 'for-each', 'force', 'format',
        'fourth', 'fprintf', 'free-identifier=?', 'free-label-identifier=?',
        'free-template-identifier=?', 'free-transformer-identifier=?',
        'fsemaphore-count', 'fsemaphore-post', 'fsemaphore-try-wait?',
        'fsemaphore-wait', 'fsemaphore?', 'future', 'future?',
        'futures-enabled?', 'gcd', 'generate-member-key',
        'generate-temporaries', 'generic-set?', 'generic?', 'gensym',
        'get-output-bytes', 'get-output-string', 'get-preference',
        'get/build-val-first-projection', 'getenv',
        'global-port-print-handler', 'group-execute-bit', 'group-read-bit',
        'group-write-bit', 'guard-evt', 'handle-evt', 'handle-evt?',
        'has-contract?', 'hash', 'hash->list', 'hash-clear', 'hash-clear!',
        'hash-copy', 'hash-copy-clear', 'hash-count', 'hash-empty?',
        'hash-eq?', 'hash-equal?', 'hash-eqv?', 'hash-for-each',
        'hash-has-key?', 'hash-iterate-first', 'hash-iterate-key',
        'hash-iterate-next', 'hash-iterate-value', 'hash-keys', 'hash-map',
        'hash-placeholder?', 'hash-ref', 'hash-ref!', 'hash-remove',
        'hash-remove!', 'hash-set', 'hash-set!', 'hash-set*', 'hash-set*!',
        'hash-update', 'hash-update!', 'hash-values', 'hash-weak?', 'hash/c',
        'hash?', 'hasheq', 'hasheqv', 'identifier-binding',
        'identifier-binding-symbol', 'identifier-label-binding',
        'identifier-prune-lexical-context',
        'identifier-prune-to-source-module',
        'identifier-remove-from-definition-context',
        'identifier-template-binding', 'identifier-transformer-binding',
        'identifier?', 'identity', 'imag-part', 'immutable?',
        'impersonate-box', 'impersonate-channel',
        'impersonate-continuation-mark-key', 'impersonate-hash',
        'impersonate-procedure', 'impersonate-prompt-tag',
        'impersonate-struct', 'impersonate-vector', 'impersonator-contract?',
        'impersonator-ephemeron', 'impersonator-of?',
        'impersonator-prop:application-mark', 'impersonator-prop:contracted',
        'impersonator-property-accessor-procedure?', 'impersonator-property?',
        'impersonator?', 'implementation?', 'implementation?/c', 'in-bytes',
        'in-bytes-lines', 'in-cycle', 'in-dict', 'in-dict-keys',
        'in-dict-pairs', 'in-dict-values', 'in-directory', 'in-hash',
        'in-hash-keys', 'in-hash-pairs', 'in-hash-values', 'in-indexed',
        'in-input-port-bytes', 'in-input-port-chars', 'in-lines', 'in-list',
        'in-mlist', 'in-naturals', 'in-parallel', 'in-permutations', 'in-port',
        'in-producer', 'in-range', 'in-sequences', 'in-set', 'in-stream',
        'in-string', 'in-value', 'in-values*-sequence', 'in-values-sequence',
        'in-vector', 'inexact->exact', 'inexact-real?', 'inexact?',
        'infinite?', 'input-port-append', 'input-port?', 'inspector?',
        'instanceof/c', 'integer->char', 'integer->integer-bytes',
        'integer-bytes->integer', 'integer-in', 'integer-length',
        'integer-sqrt', 'integer-sqrt/remainder', 'integer?',
        'interface->method-names', 'interface-extension?', 'interface?',
        'internal-definition-context-seal', 'internal-definition-context?',
        'is-a?', 'is-a?/c', 'keyword->string', 'keyword-apply', 'keyword<?',
        'keyword?', 'keywords-match', 'kill-thread', 'last', 'last-pair',
        'lcm', 'length', 'liberal-define-context?', 'link-exists?', 'list',
        'list*', 'list->bytes', 'list->mutable-set', 'list->mutable-seteq',
        'list->mutable-seteqv', 'list->set', 'list->seteq', 'list->seteqv',
        'list->string', 'list->vector', 'list->weak-set', 'list->weak-seteq',
        'list->weak-seteqv', 'list-ref', 'list-tail', 'list/c', 'list?',
        'listof', 'load', 'load-extension', 'load-on-demand-enabled',
        'load-relative', 'load-relative-extension', 'load/cd',
        'load/use-compiled', 'local-expand', 'local-expand/capture-lifts',
        'local-transformer-expand', 'local-transformer-expand/capture-lifts',
        'locale-string-encoding', 'log', 'log-level?', 'log-max-level',
        'log-message', 'log-receiver?', 'logger-name', 'logger?', 'magnitude',
        'make-arity-at-least', 'make-base-empty-namespace',
        'make-base-namespace', 'make-bytes', 'make-channel',
        'make-chaperone-contract', 'make-continuation-mark-key',
        'make-continuation-prompt-tag', 'make-contract', 'make-custodian',
        'make-custodian-box', 'make-custom-hash', 'make-custom-hash-types',
        'make-custom-set', 'make-custom-set-types', 'make-date', 'make-date*',
        'make-derived-parameter', 'make-directory', 'make-directory*',
        'make-do-sequence', 'make-empty-namespace',
        'make-environment-variables', 'make-ephemeron', 'make-exn',
        'make-exn:break', 'make-exn:break:hang-up', 'make-exn:break:terminate',
        'make-exn:fail', 'make-exn:fail:contract',
        'make-exn:fail:contract:arity', 'make-exn:fail:contract:blame',
        'make-exn:fail:contract:continuation',
        'make-exn:fail:contract:divide-by-zero',
        'make-exn:fail:contract:non-fixnum-result',
        'make-exn:fail:contract:variable', 'make-exn:fail:filesystem',
        'make-exn:fail:filesystem:errno', 'make-exn:fail:filesystem:exists',
        'make-exn:fail:filesystem:missing-module',
        'make-exn:fail:filesystem:version', 'make-exn:fail:network',
        'make-exn:fail:network:errno', 'make-exn:fail:object',
        'make-exn:fail:out-of-memory', 'make-exn:fail:read',
        'make-exn:fail:read:eof', 'make-exn:fail:read:non-char',
        'make-exn:fail:syntax', 'make-exn:fail:syntax:missing-module',
        'make-exn:fail:syntax:unbound', 'make-exn:fail:unsupported',
        'make-exn:fail:user', 'make-file-or-directory-link',
        'make-flat-contract', 'make-fsemaphore', 'make-generic',
        'make-handle-get-preference-locked', 'make-hash',
        'make-hash-placeholder', 'make-hasheq', 'make-hasheq-placeholder',
        'make-hasheqv', 'make-hasheqv-placeholder',
        'make-immutable-custom-hash', 'make-immutable-hash',
        'make-immutable-hasheq', 'make-immutable-hasheqv',
        'make-impersonator-property', 'make-input-port',
        'make-input-port/read-to-peek', 'make-inspector',
        'make-keyword-procedure', 'make-known-char-range-list',
        'make-limited-input-port', 'make-list', 'make-lock-file-name',
        'make-log-receiver', 'make-logger', 'make-mixin-contract',
        'make-mutable-custom-set', 'make-none/c', 'make-object',
        'make-output-port', 'make-parameter', 'make-phantom-bytes',
        'make-pipe', 'make-pipe-with-specials', 'make-placeholder',
        'make-polar', 'make-prefab-struct', 'make-primitive-class',
        'make-proj-contract', 'make-pseudo-random-generator',
        'make-reader-graph', 'make-readtable', 'make-rectangular',
        'make-rename-transformer', 'make-resolved-module-path',
        'make-security-guard', 'make-semaphore', 'make-set!-transformer',
        'make-shared-bytes', 'make-sibling-inspector', 'make-special-comment',
        'make-srcloc', 'make-string', 'make-struct-field-accessor',
        'make-struct-field-mutator', 'make-struct-type',
        'make-struct-type-property', 'make-syntax-delta-introducer',
        'make-syntax-introducer', 'make-temporary-file',
        'make-tentative-pretty-print-output-port', 'make-thread-cell',
        'make-thread-group', 'make-vector', 'make-weak-box',
        'make-weak-custom-hash', 'make-weak-custom-set', 'make-weak-hash',
        'make-weak-hasheq', 'make-weak-hasheqv', 'make-will-executor', 'map',
        'match-equality-test', 'matches-arity-exactly?', 'max', 'mcar', 'mcdr',
        'mcons', 'member', 'member-name-key-hash-code', 'member-name-key=?',
        'member-name-key?', 'memf', 'memq', 'memv', 'merge-input',
        'method-in-interface?', 'min', 'mixin-contract', 'module->exports',
        'module->imports', 'module->language-info', 'module->namespace',
        'module-compiled-cross-phase-persistent?', 'module-compiled-exports',
        'module-compiled-imports', 'module-compiled-language-info',
        'module-compiled-name', 'module-compiled-submodules',
        'module-declared?', 'module-path-index-join',
        'module-path-index-resolve', 'module-path-index-split',
        'module-path-index-submodule', 'module-path-index?', 'module-path?',
        'module-predefined?', 'module-provide-protected?', 'modulo', 'mpair?',
        'mutable-set', 'mutable-seteq', 'mutable-seteqv', 'n->th',
        'nack-guard-evt', 'namespace-anchor->empty-namespace',
        'namespace-anchor->namespace', 'namespace-anchor?',
        'namespace-attach-module', 'namespace-attach-module-declaration',
        'namespace-base-phase', 'namespace-mapped-symbols',
        'namespace-module-identifier', 'namespace-module-registry',
        'namespace-require', 'namespace-require/constant',
        'namespace-require/copy', 'namespace-require/expansion-time',
        'namespace-set-variable-value!', 'namespace-symbol->identifier',
        'namespace-syntax-introduce', 'namespace-undefine-variable!',
        'namespace-unprotect-module', 'namespace-variable-value', 'namespace?',
        'nan?', 'natural-number/c', 'negate', 'negative?', 'never-evt',
        u'new-∀/c', u'new-∃/c', 'newline', 'ninth', 'non-empty-listof',
        'none/c', 'normal-case-path', 'normalize-arity', 'normalize-path',
        'normalized-arity?', 'not', 'not/c', 'null', 'null?', 'number->string',
        'number?', 'numerator', 'object%', 'object->vector', 'object-info',
        'object-interface', 'object-method-arity-includes?', 'object-name',
        'object=?', 'object?', 'odd?', 'one-of/c', 'open-input-bytes',
        'open-input-file', 'open-input-output-file', 'open-input-string',
        'open-output-bytes', 'open-output-file', 'open-output-nowhere',
        'open-output-string', 'or/c', 'order-of-magnitude', 'ormap',
        'other-execute-bit', 'other-read-bit', 'other-write-bit',
        'output-port?', 'pair?', 'parameter-procedure=?', 'parameter/c',
        'parameter?', 'parameterization?', 'parse-command-line', 'partition',
        'path->bytes', 'path->complete-path', 'path->directory-path',
        'path->string', 'path-add-suffix', 'path-convention-type',
        'path-element->bytes', 'path-element->string', 'path-element?',
        'path-for-some-system?', 'path-list-string->path-list', 'path-only',
        'path-replace-suffix', 'path-string?', 'path<?', 'path?',
        'pathlist-closure', 'peek-byte', 'peek-byte-or-special', 'peek-bytes',
        'peek-bytes!', 'peek-bytes!-evt', 'peek-bytes-avail!',
        'peek-bytes-avail!*', 'peek-bytes-avail!-evt',
        'peek-bytes-avail!/enable-break', 'peek-bytes-evt', 'peek-char',
        'peek-char-or-special', 'peek-string', 'peek-string!',
        'peek-string!-evt', 'peek-string-evt', 'peeking-input-port',
        'permutations', 'phantom-bytes?', 'pi', 'pi.f', 'pipe-content-length',
        'place-break', 'place-channel', 'place-channel-get',
        'place-channel-put', 'place-channel-put/get', 'place-channel?',
        'place-dead-evt', 'place-enabled?', 'place-kill', 'place-location?',
        'place-message-allowed?', 'place-sleep', 'place-wait', 'place?',
        'placeholder-get', 'placeholder-set!', 'placeholder?',
        'poll-guard-evt', 'port->bytes', 'port->bytes-lines', 'port->lines',
        'port->list', 'port->string', 'port-closed-evt', 'port-closed?',
        'port-commit-peeked', 'port-count-lines!', 'port-count-lines-enabled',
        'port-counts-lines?', 'port-display-handler', 'port-file-identity',
        'port-file-unlock', 'port-next-location', 'port-print-handler',
        'port-progress-evt', 'port-provides-progress-evts?',
        'port-read-handler', 'port-try-file-lock?', 'port-write-handler',
        'port-writes-atomic?', 'port-writes-special?', 'port?', 'positive?',
        'predicate/c', 'prefab-key->struct-type', 'prefab-key?',
        'prefab-struct-key', 'preferences-lock-file-mode', 'pregexp',
        'pregexp?', 'pretty-display', 'pretty-format', 'pretty-print',
        'pretty-print-.-symbol-without-bars',
        'pretty-print-abbreviate-read-macros', 'pretty-print-columns',
        'pretty-print-current-style-table', 'pretty-print-depth',
        'pretty-print-exact-as-decimal', 'pretty-print-extend-style-table',
        'pretty-print-handler', 'pretty-print-newline',
        'pretty-print-post-print-hook', 'pretty-print-pre-print-hook',
        'pretty-print-print-hook', 'pretty-print-print-line',
        'pretty-print-remap-stylable', 'pretty-print-show-inexactness',
        'pretty-print-size-hook', 'pretty-print-style-table?',
        'pretty-printing', 'pretty-write', 'primitive-closure?',
        'primitive-result-arity', 'primitive?', 'print', 'print-as-expression',
        'print-boolean-long-form', 'print-box', 'print-graph',
        'print-hash-table', 'print-mpair-curly-braces',
        'print-pair-curly-braces', 'print-reader-abbreviations',
        'print-struct', 'print-syntax-width', 'print-unreadable',
        'print-vector-length', 'printable/c', 'printable<%>', 'printf',
        'procedure->method', 'procedure-arity', 'procedure-arity-includes/c',
        'procedure-arity-includes?', 'procedure-arity?',
        'procedure-closure-contents-eq?', 'procedure-extract-target',
        'procedure-keywords', 'procedure-reduce-arity',
        'procedure-reduce-keyword-arity', 'procedure-rename',
        'procedure-struct-type?', 'procedure?', 'process', 'process*',
        'process*/ports', 'process/ports', 'processor-count', 'progress-evt?',
        'promise-forced?', 'promise-running?', 'promise/c', 'promise?',
        'prop:arity-string', 'prop:chaperone-contract',
        'prop:checked-procedure', 'prop:contract', 'prop:contracted',
        'prop:custom-print-quotable', 'prop:custom-write', 'prop:dict',
        'prop:dict/contract', 'prop:equal+hash', 'prop:evt',
        'prop:exn:missing-module', 'prop:exn:srclocs', 'prop:flat-contract',
        'prop:impersonator-of', 'prop:input-port',
        'prop:liberal-define-context', 'prop:opt-chaperone-contract',
        'prop:opt-chaperone-contract-get-test', 'prop:opt-chaperone-contract?',
        'prop:output-port', 'prop:place-location', 'prop:procedure',
        'prop:rename-transformer', 'prop:sequence', 'prop:set!-transformer',
        'prop:stream', 'proper-subset?', 'pseudo-random-generator->vector',
        'pseudo-random-generator-vector?', 'pseudo-random-generator?',
        'put-preferences', 'putenv', 'quotient', 'quotient/remainder',
        'radians->degrees', 'raise', 'raise-argument-error',
        'raise-arguments-error', 'raise-arity-error', 'raise-blame-error',
        'raise-contract-error', 'raise-mismatch-error',
        'raise-not-cons-blame-error', 'raise-range-error',
        'raise-result-error', 'raise-syntax-error', 'raise-type-error',
        'raise-user-error', 'random', 'random-seed', 'range', 'rational?',
        'rationalize', 'read', 'read-accept-bar-quote', 'read-accept-box',
        'read-accept-compiled', 'read-accept-dot', 'read-accept-graph',
        'read-accept-infix-dot', 'read-accept-lang', 'read-accept-quasiquote',
        'read-accept-reader', 'read-byte', 'read-byte-or-special',
        'read-bytes', 'read-bytes!', 'read-bytes!-evt', 'read-bytes-avail!',
        'read-bytes-avail!*', 'read-bytes-avail!-evt',
        'read-bytes-avail!/enable-break', 'read-bytes-evt', 'read-bytes-line',
        'read-bytes-line-evt', 'read-case-sensitive', 'read-char',
        'read-char-or-special', 'read-curly-brace-as-paren',
        'read-decimal-as-inexact', 'read-eval-print-loop', 'read-language',
        'read-line', 'read-line-evt', 'read-on-demand-source',
        'read-square-bracket-as-paren', 'read-string', 'read-string!',
        'read-string!-evt', 'read-string-evt', 'read-syntax',
        'read-syntax/recursive', 'read/recursive', 'readtable-mapping',
        'readtable?', 'real->decimal-string', 'real->double-flonum',
        'real->floating-point-bytes', 'real->single-flonum', 'real-in',
        'real-part', 'real?', 'reencode-input-port', 'reencode-output-port',
        'regexp', 'regexp-match', 'regexp-match*', 'regexp-match-evt',
        'regexp-match-exact?', 'regexp-match-peek',
        'regexp-match-peek-immediate', 'regexp-match-peek-positions',
        'regexp-match-peek-positions*',
        'regexp-match-peek-positions-immediate',
        'regexp-match-peek-positions-immediate/end',
        'regexp-match-peek-positions/end', 'regexp-match-positions',
        'regexp-match-positions*', 'regexp-match-positions/end',
        'regexp-match/end', 'regexp-match?', 'regexp-max-lookbehind',
        'regexp-quote', 'regexp-replace', 'regexp-replace*',
        'regexp-replace-quote', 'regexp-replaces', 'regexp-split',
        'regexp-try-match', 'regexp?', 'relative-path?', 'relocate-input-port',
        'relocate-output-port', 'remainder', 'remove', 'remove*',
        'remove-duplicates', 'remq', 'remq*', 'remv', 'remv*',
        'rename-file-or-directory', 'rename-transformer-target',
        'rename-transformer?', 'reroot-path', 'resolve-path',
        'resolved-module-path-name', 'resolved-module-path?', 'rest',
        'reverse', 'round', 'second', 'seconds->date', 'security-guard?',
        'semaphore-peek-evt', 'semaphore-peek-evt?', 'semaphore-post',
        'semaphore-try-wait?', 'semaphore-wait', 'semaphore-wait/enable-break',
        'semaphore?', 'sequence->list', 'sequence->stream',
        'sequence-add-between', 'sequence-andmap', 'sequence-append',
        'sequence-count', 'sequence-filter', 'sequence-fold',
        'sequence-for-each', 'sequence-generate', 'sequence-generate*',
        'sequence-length', 'sequence-map', 'sequence-ormap', 'sequence-ref',
        'sequence-tail', 'sequence?', 'set', 'set!-transformer-procedure',
        'set!-transformer?', 'set->list', 'set->stream', 'set-add', 'set-add!',
        'set-box!', 'set-clear', 'set-clear!', 'set-copy', 'set-copy-clear',
        'set-count', 'set-empty?', 'set-eq?', 'set-equal?', 'set-eqv?',
        'set-first', 'set-for-each', 'set-implements/c', 'set-implements?',
        'set-intersect', 'set-intersect!', 'set-map', 'set-mcar!', 'set-mcdr!',
        'set-member?', 'set-mutable?', 'set-phantom-bytes!',
        'set-port-next-location!', 'set-remove', 'set-remove!', 'set-rest',
        'set-subtract', 'set-subtract!', 'set-symmetric-difference',
        'set-symmetric-difference!', 'set-union', 'set-union!', 'set-weak?',
        'set/c', 'set=?', 'set?', 'seteq', 'seteqv', 'seventh', 'sgn',
        'shared-bytes', 'shell-execute', 'shrink-path-wrt', 'shuffle',
        'simple-form-path', 'simplify-path', 'sin', 'single-flonum?', 'sinh',
        'sixth', 'skip-projection-wrapper?', 'sleep',
        'some-system-path->string', 'sort', 'special-comment-value',
        'special-comment?', 'special-filter-input-port', 'split-at',
        'split-at-right', 'split-path', 'splitf-at', 'splitf-at-right', 'sqr',
        'sqrt', 'srcloc', 'srcloc->string', 'srcloc-column', 'srcloc-line',
        'srcloc-position', 'srcloc-source', 'srcloc-span', 'srcloc?',
        'stop-after', 'stop-before', 'stream->list', 'stream-add-between',
        'stream-andmap', 'stream-append', 'stream-count', 'stream-empty?',
        'stream-filter', 'stream-first', 'stream-fold', 'stream-for-each',
        'stream-length', 'stream-map', 'stream-ormap', 'stream-ref',
        'stream-rest', 'stream-tail', 'stream?', 'string',
        'string->bytes/latin-1', 'string->bytes/locale', 'string->bytes/utf-8',
        'string->immutable-string', 'string->keyword', 'string->list',
        'string->number', 'string->path', 'string->path-element',
        'string->some-system-path', 'string->symbol',
        'string->uninterned-symbol', 'string->unreadable-symbol',
        'string-append', 'string-append*', 'string-ci<=?', 'string-ci<?',
        'string-ci=?', 'string-ci>=?', 'string-ci>?', 'string-copy',
        'string-copy!', 'string-downcase', 'string-environment-variable-name?',
        'string-fill!', 'string-foldcase', 'string-join', 'string-len/c',
        'string-length', 'string-locale-ci<?', 'string-locale-ci=?',
        'string-locale-ci>?', 'string-locale-downcase', 'string-locale-upcase',
        'string-locale<?', 'string-locale=?', 'string-locale>?',
        'string-no-nuls?', 'string-normalize-nfc', 'string-normalize-nfd',
        'string-normalize-nfkc', 'string-normalize-nfkd',
        'string-normalize-spaces', 'string-ref', 'string-replace',
        'string-set!', 'string-split', 'string-titlecase', 'string-trim',
        'string-upcase', 'string-utf-8-length', 'string<=?', 'string<?',
        'string=?', 'string>=?', 'string>?', 'string?', 'struct->vector',
        'struct-accessor-procedure?', 'struct-constructor-procedure?',
        'struct-info', 'struct-mutator-procedure?',
        'struct-predicate-procedure?', 'struct-type-info',
        'struct-type-make-constructor', 'struct-type-make-predicate',
        'struct-type-property-accessor-procedure?', 'struct-type-property/c',
        'struct-type-property?', 'struct-type?', 'struct:arity-at-least',
        'struct:date', 'struct:date*', 'struct:exn', 'struct:exn:break',
        'struct:exn:break:hang-up', 'struct:exn:break:terminate',
        'struct:exn:fail', 'struct:exn:fail:contract',
        'struct:exn:fail:contract:arity', 'struct:exn:fail:contract:blame',
        'struct:exn:fail:contract:continuation',
        'struct:exn:fail:contract:divide-by-zero',
        'struct:exn:fail:contract:non-fixnum-result',
        'struct:exn:fail:contract:variable', 'struct:exn:fail:filesystem',
        'struct:exn:fail:filesystem:errno',
        'struct:exn:fail:filesystem:exists',
        'struct:exn:fail:filesystem:missing-module',
        'struct:exn:fail:filesystem:version', 'struct:exn:fail:network',
        'struct:exn:fail:network:errno', 'struct:exn:fail:object',
        'struct:exn:fail:out-of-memory', 'struct:exn:fail:read',
        'struct:exn:fail:read:eof', 'struct:exn:fail:read:non-char',
        'struct:exn:fail:syntax', 'struct:exn:fail:syntax:missing-module',
        'struct:exn:fail:syntax:unbound', 'struct:exn:fail:unsupported',
        'struct:exn:fail:user', 'struct:srcloc',
        'struct:wrapped-extra-arg-arrow', 'struct?', 'sub1', 'subbytes',
        'subclass?', 'subclass?/c', 'subprocess', 'subprocess-group-enabled',
        'subprocess-kill', 'subprocess-pid', 'subprocess-status',
        'subprocess-wait', 'subprocess?', 'subset?', 'substring',
        'symbol->string', 'symbol-interned?', 'symbol-unreadable?', 'symbol<?',
        'symbol=?', 'symbol?', 'symbols', 'sync', 'sync/enable-break',
        'sync/timeout', 'sync/timeout/enable-break', 'syntax->datum',
        'syntax->list', 'syntax-arm', 'syntax-column', 'syntax-disarm',
        'syntax-e', 'syntax-line', 'syntax-local-bind-syntaxes',
        'syntax-local-certifier', 'syntax-local-context',
        'syntax-local-expand-expression', 'syntax-local-get-shadower',
        'syntax-local-introduce', 'syntax-local-lift-context',
        'syntax-local-lift-expression',
        'syntax-local-lift-module-end-declaration',
        'syntax-local-lift-provide', 'syntax-local-lift-require',
        'syntax-local-lift-values-expression',
        'syntax-local-make-definition-context',
        'syntax-local-make-delta-introducer',
        'syntax-local-module-defined-identifiers',
        'syntax-local-module-exports',
        'syntax-local-module-required-identifiers', 'syntax-local-name',
        'syntax-local-phase-level', 'syntax-local-submodules',
        'syntax-local-transforming-module-provides?', 'syntax-local-value',
        'syntax-local-value/immediate', 'syntax-original?', 'syntax-position',
        'syntax-property', 'syntax-property-symbol-keys', 'syntax-protect',
        'syntax-rearm', 'syntax-recertify', 'syntax-shift-phase-level',
        'syntax-source', 'syntax-source-module', 'syntax-span', 'syntax-taint',
        'syntax-tainted?', 'syntax-track-origin',
        'syntax-transforming-module-expression?', 'syntax-transforming?',
        'syntax/c', 'syntax?', 'system', 'system*', 'system*/exit-code',
        'system-big-endian?', 'system-idle-evt', 'system-language+country',
        'system-library-subpath', 'system-path-convention-type', 'system-type',
        'system/exit-code', 'tail-marks-match?', 'take', 'take-right', 'takef',
        'takef-right', 'tan', 'tanh', 'tcp-abandon-port', 'tcp-accept',
        'tcp-accept-evt', 'tcp-accept-ready?', 'tcp-accept/enable-break',
        'tcp-addresses', 'tcp-close', 'tcp-connect',
        'tcp-connect/enable-break', 'tcp-listen', 'tcp-listener?', 'tcp-port?',
        'tentative-pretty-print-port-cancel',
        'tentative-pretty-print-port-transfer', 'tenth', 'terminal-port?',
        'the-unsupplied-arg', 'third', 'thread', 'thread-cell-ref',
        'thread-cell-set!', 'thread-cell-values?', 'thread-cell?',
        'thread-dead-evt', 'thread-dead?', 'thread-group?', 'thread-receive',
        'thread-receive-evt', 'thread-resume', 'thread-resume-evt',
        'thread-rewind-receive', 'thread-running?', 'thread-send',
        'thread-suspend', 'thread-suspend-evt', 'thread-try-receive',
        'thread-wait', 'thread/suspend-to-kill', 'thread?', 'time-apply',
        'touch', 'transplant-input-port', 'transplant-output-port', 'true',
        'truncate', 'udp-addresses', 'udp-bind!', 'udp-bound?', 'udp-close',
        'udp-connect!', 'udp-connected?', 'udp-multicast-interface',
        'udp-multicast-join-group!', 'udp-multicast-leave-group!',
        'udp-multicast-loopback?', 'udp-multicast-set-interface!',
        'udp-multicast-set-loopback!', 'udp-multicast-set-ttl!',
        'udp-multicast-ttl', 'udp-open-socket', 'udp-receive!',
        'udp-receive!*', 'udp-receive!-evt', 'udp-receive!/enable-break',
        'udp-receive-ready-evt', 'udp-send', 'udp-send*', 'udp-send-evt',
        'udp-send-ready-evt', 'udp-send-to', 'udp-send-to*', 'udp-send-to-evt',
        'udp-send-to/enable-break', 'udp-send/enable-break', 'udp?', 'unbox',
        'uncaught-exception-handler', 'unit?', 'unspecified-dom',
        'unsupplied-arg?', 'use-collection-link-paths',
        'use-compiled-file-paths', 'use-user-specific-search-paths',
        'user-execute-bit', 'user-read-bit', 'user-write-bit',
        'value-contract', 'values', 'variable-reference->empty-namespace',
        'variable-reference->module-base-phase',
        'variable-reference->module-declaration-inspector',
        'variable-reference->module-path-index',
        'variable-reference->module-source', 'variable-reference->namespace',
        'variable-reference->phase',
        'variable-reference->resolved-module-path',
        'variable-reference-constant?', 'variable-reference?', 'vector',
        'vector->immutable-vector', 'vector->list',
        'vector->pseudo-random-generator', 'vector->pseudo-random-generator!',
        'vector->values', 'vector-append', 'vector-argmax', 'vector-argmin',
        'vector-copy', 'vector-copy!', 'vector-count', 'vector-drop',
        'vector-drop-right', 'vector-fill!', 'vector-filter',
        'vector-filter-not', 'vector-immutable', 'vector-immutable/c',
        'vector-immutableof', 'vector-length', 'vector-map', 'vector-map!',
        'vector-member', 'vector-memq', 'vector-memv', 'vector-ref',
        'vector-set!', 'vector-set*!', 'vector-set-performance-stats!',
        'vector-split-at', 'vector-split-at-right', 'vector-take',
        'vector-take-right', 'vector/c', 'vector?', 'vectorof', 'version',
        'void', 'void?', 'weak-box-value', 'weak-box?', 'weak-set',
        'weak-seteq', 'weak-seteqv', 'will-execute', 'will-executor?',
        'will-register', 'will-try-execute', 'with-input-from-bytes',
        'with-input-from-file', 'with-input-from-string',
        'with-output-to-bytes', 'with-output-to-file', 'with-output-to-string',
        'would-be-future', 'wrap-evt', 'wrapped-extra-arg-arrow',
        'wrapped-extra-arg-arrow-extra-neg-party-argument',
        'wrapped-extra-arg-arrow-real-func', 'wrapped-extra-arg-arrow?',
        'writable<%>', 'write', 'write-byte', 'write-bytes',
        'write-bytes-avail', 'write-bytes-avail*', 'write-bytes-avail-evt',
        'write-bytes-avail/enable-break', 'write-char', 'write-special',
        'write-special-avail*', 'write-special-evt', 'write-string',
        'write-to-file', 'xor', 'zero?', '~.a', '~.s', '~.v', '~a', '~e', '~r',
        '~s', '~v'
    )

    _opening_parenthesis = r'[([{]'
    _closing_parenthesis = r'[)\]}]'
    _delimiters = r'()[\]{}",\'`;\s'
    _symbol = r'(?u)(?:\|[^|]*\||\\[\w\W]|[^|\\%s]+)+' % _delimiters
    _exact_decimal_prefix = r'(?:#e)?(?:#d)?(?:#e)?'
    _exponent = r'(?:[defls][-+]?\d+)'
    _inexact_simple_no_hashes = r'(?:\d+(?:/\d+|\.\d*)?|\.\d+)'
    _inexact_simple = (r'(?:%s|(?:\d+#+(?:\.#*|/\d+#*)?|\.\d+#+|'
                       r'\d+(?:\.\d*#+|/\d+#+)))' % _inexact_simple_no_hashes)
    _inexact_normal_no_hashes = r'(?:%s%s?)' % (_inexact_simple_no_hashes,
                                                _exponent)
    _inexact_normal = r'(?:%s%s?)' % (_inexact_simple, _exponent)
    _inexact_special = r'(?:(?:inf|nan)\.[0f])'
    _inexact_real = r'(?:[-+]?%s|[-+]%s)' % (_inexact_normal,
                                             _inexact_special)
    _inexact_unsigned = r'(?:%s|%s)' % (_inexact_normal, _inexact_special)

    tokens = {
        'root': [
            (_closing_parenthesis, Error),
            (r'(?!\Z)', Text, 'unquoted-datum')
        ],
        'datum': [
            (r'(?s)#;|#![ /]([^\\\n]|\\.)*', Comment),
            (u';[^\\n\\r\x85\u2028\u2029]*', Comment.Single),
            (r'#\|', Comment.Multiline, 'block-comment'),

            # Whitespaces
            (r'(?u)\s+', Text),

            # Numbers: Keep in mind Racket reader hash prefixes, which
            # can denote the base or the type. These don't map neatly
            # onto Pygments token types; some judgment calls here.

            # #d or no prefix
            (r'(?i)%s[-+]?\d+(?=[%s])' % (_exact_decimal_prefix, _delimiters),
             Number.Integer, '#pop'),
            (r'(?i)%s[-+]?(\d+(\.\d*)?|\.\d+)([deflst][-+]?\d+)?(?=[%s])' %
             (_exact_decimal_prefix, _delimiters), Number.Float, '#pop'),
            (r'(?i)%s[-+]?(%s([-+]%s?i)?|[-+]%s?i)(?=[%s])' %
             (_exact_decimal_prefix, _inexact_normal_no_hashes,
              _inexact_normal_no_hashes, _inexact_normal_no_hashes,
              _delimiters), Number, '#pop'),

            # Inexact without explicit #i
            (r'(?i)(#d)?(%s([-+]%s?i)?|[-+]%s?i|%s@%s)(?=[%s])' %
             (_inexact_real, _inexact_unsigned, _inexact_unsigned,
              _inexact_real, _inexact_real, _delimiters), Number.Float,
             '#pop'),

            # The remaining extflonums
            (r'(?i)(([-+]?%st[-+]?\d+)|[-+](inf|nan)\.t)(?=[%s])' %
             (_inexact_simple, _delimiters), Number.Float, '#pop'),

            # #b
            (r'(?i)(#[ei])?#b%s' % _symbol, Number.Bin, '#pop'),

            # #o
            (r'(?i)(#[ei])?#o%s' % _symbol, Number.Oct, '#pop'),

            # #x
            (r'(?i)(#[ei])?#x%s' % _symbol, Number.Hex, '#pop'),

            # #i is always inexact, i.e. float
            (r'(?i)(#d)?#i%s' % _symbol, Number.Float, '#pop'),

            # Strings and characters
            (r'#?"', String.Double, ('#pop', 'string')),
            (r'#<<(.+)\n(^(?!\1$).*$\n)*^\1$', String.Heredoc, '#pop'),
            (r'#\\(u[\da-fA-F]{1,4}|U[\da-fA-F]{1,8})', String.Char, '#pop'),
            (r'(?is)#\\([0-7]{3}|[a-z]+|.)', String.Char, '#pop'),
            (r'(?s)#[pr]x#?"(\\?.)*?"', String.Regex, '#pop'),

            # Constants
            (r'#(true|false|[tTfF])', Name.Constant, '#pop'),

            # Keyword argument names (e.g. #:keyword)
            (r'#:%s' % _symbol, Keyword.Declaration, '#pop'),

            # Reader extensions
            (r'(#lang |#!)(\S+)',
             bygroups(Keyword.Namespace, Name.Namespace)),
            (r'#reader', Keyword.Namespace, 'quoted-datum'),

            # Other syntax
            (r"(?i)\.(?=[%s])|#c[is]|#['`]|#,@?" % _delimiters, Operator),
            (r"'|#[s&]|#hash(eqv?)?|#\d*(?=%s)" % _opening_parenthesis,
             Operator, ('#pop', 'quoted-datum'))
        ],
        'datum*': [
            (r'`|,@?', Operator),
            (_symbol, String.Symbol, '#pop'),
            (r'[|\\]', Error),
            default('#pop')
        ],
        'list': [
            (_closing_parenthesis, Punctuation, '#pop')
        ],
        'unquoted-datum': [
            include('datum'),
            (r'quote(?=[%s])' % _delimiters, Keyword,
             ('#pop', 'quoted-datum')),
            (r'`', Operator, ('#pop', 'quasiquoted-datum')),
            (r'quasiquote(?=[%s])' % _delimiters, Keyword,
             ('#pop', 'quasiquoted-datum')),
            (_opening_parenthesis, Punctuation, ('#pop', 'unquoted-list')),
            (words(_keywords, prefix='(?u)', suffix='(?=[%s])' % _delimiters),
             Keyword, '#pop'),
            (words(_builtins, prefix='(?u)', suffix='(?=[%s])' % _delimiters),
             Name.Builtin, '#pop'),
            (_symbol, Name, '#pop'),
            include('datum*')
        ],
        'unquoted-list': [
            include('list'),
            (r'(?!\Z)', Text, 'unquoted-datum')
        ],
        'quasiquoted-datum': [
            include('datum'),
            (r',@?', Operator, ('#pop', 'unquoted-datum')),
            (r'unquote(-splicing)?(?=[%s])' % _delimiters, Keyword,
             ('#pop', 'unquoted-datum')),
            (_opening_parenthesis, Punctuation, ('#pop', 'quasiquoted-list')),
            include('datum*')
        ],
        'quasiquoted-list': [
            include('list'),
            (r'(?!\Z)', Text, 'quasiquoted-datum')
        ],
        'quoted-datum': [
            include('datum'),
            (_opening_parenthesis, Punctuation, ('#pop', 'quoted-list')),
            include('datum*')
        ],
        'quoted-list': [
            include('list'),
            (r'(?!\Z)', Text, 'quoted-datum')
        ],
        'block-comment': [
            (r'#\|', Comment.Multiline, '#push'),
            (r'\|#', Comment.Multiline, '#pop'),
            (r'[^#|]+|.', Comment.Multiline)
        ],
        'string': [
            (r'"', String.Double, '#pop'),
            (r'(?s)\\([0-7]{1,3}|x[\da-fA-F]{1,2}|u[\da-fA-F]{1,4}|'
             r'U[\da-fA-F]{1,8}|.)', String.Escape),
            (r'[^\\"]+', String.Double)
        ]
    }


class NewLispLexer(RegexLexer):
    """
    For `newLISP. <www.newlisp.org>`_ source code (version 10.3.0).

    .. versionadded:: 1.5
    """

    name = 'NewLisp'
    aliases = ['newlisp']
    filenames = ['*.lsp', '*.nl']
    mimetypes = ['text/x-newlisp', 'application/x-newlisp']

    flags = re.IGNORECASE | re.MULTILINE | re.UNICODE

    # list of built-in functions for newLISP version 10.3
    builtins = (
        '^', '--', '-', ':', '!', '!=', '?', '@', '*', '/', '&', '%', '+', '++',
        '<', '<<', '<=', '=', '>', '>=', '>>', '|', '~', '$', '$0', '$1', '$10',
        '$11', '$12', '$13', '$14', '$15', '$2', '$3', '$4', '$5', '$6', '$7',
        '$8', '$9', '$args', '$idx', '$it', '$main-args', 'abort', 'abs',
        'acos', 'acosh', 'add', 'address', 'amb', 'and',  'append-file',
        'append', 'apply', 'args', 'array-list', 'array?', 'array', 'asin',
        'asinh', 'assoc', 'atan', 'atan2', 'atanh', 'atom?', 'base64-dec',
        'base64-enc', 'bayes-query', 'bayes-train', 'begin',
        'beta', 'betai', 'bind', 'binomial', 'bits', 'callback',
        'case', 'catch', 'ceil', 'change-dir', 'char', 'chop', 'Class', 'clean',
        'close', 'command-event', 'cond', 'cons', 'constant',
        'context?', 'context', 'copy-file', 'copy', 'cos', 'cosh', 'count',
        'cpymem', 'crc32', 'crit-chi2', 'crit-z', 'current-line', 'curry',
        'date-list', 'date-parse', 'date-value', 'date', 'debug', 'dec',
        'def-new', 'default', 'define-macro', 'define',
        'delete-file', 'delete-url', 'delete', 'destroy', 'det', 'device',
        'difference', 'directory?', 'directory', 'div', 'do-until', 'do-while',
        'doargs',  'dolist',  'dostring', 'dotimes',  'dotree', 'dump', 'dup',
        'empty?', 'encrypt', 'ends-with', 'env', 'erf', 'error-event',
        'eval-string', 'eval', 'exec', 'exists', 'exit', 'exp', 'expand',
        'explode', 'extend', 'factor', 'fft', 'file-info', 'file?', 'filter',
        'find-all', 'find', 'first', 'flat', 'float?', 'float', 'floor', 'flt',
        'fn', 'for-all', 'for', 'fork', 'format', 'fv', 'gammai', 'gammaln',
        'gcd', 'get-char', 'get-float', 'get-int', 'get-long', 'get-string',
        'get-url', 'global?', 'global', 'if-not', 'if', 'ifft', 'import', 'inc',
        'index', 'inf?', 'int', 'integer?', 'integer', 'intersect', 'invert',
        'irr', 'join', 'lambda-macro', 'lambda?', 'lambda', 'last-error',
        'last', 'legal?', 'length', 'let', 'letex', 'letn',
        'list?', 'list', 'load', 'local', 'log', 'lookup',
        'lower-case', 'macro?', 'main-args', 'MAIN', 'make-dir', 'map', 'mat',
        'match', 'max', 'member', 'min', 'mod', 'module', 'mul', 'multiply',
        'NaN?', 'net-accept', 'net-close', 'net-connect', 'net-error',
        'net-eval', 'net-interface', 'net-ipv', 'net-listen', 'net-local',
        'net-lookup', 'net-packet', 'net-peek', 'net-peer', 'net-ping',
        'net-receive-from', 'net-receive-udp', 'net-receive', 'net-select',
        'net-send-to', 'net-send-udp', 'net-send', 'net-service',
        'net-sessions', 'new', 'nil?', 'nil', 'normal', 'not', 'now', 'nper',
        'npv', 'nth', 'null?', 'number?', 'open', 'or', 'ostype', 'pack',
        'parse-date', 'parse', 'peek', 'pipe', 'pmt', 'pop-assoc', 'pop',
        'post-url', 'pow', 'prefix', 'pretty-print', 'primitive?', 'print',
        'println', 'prob-chi2', 'prob-z', 'process', 'prompt-event',
        'protected?', 'push', 'put-url', 'pv', 'quote?', 'quote', 'rand',
        'random', 'randomize', 'read', 'read-char', 'read-expr', 'read-file',
        'read-key', 'read-line', 'read-utf8', 'reader-event',
        'real-path', 'receive', 'ref-all', 'ref', 'regex-comp', 'regex',
        'remove-dir', 'rename-file', 'replace', 'reset', 'rest', 'reverse',
        'rotate', 'round', 'save', 'search', 'seed', 'seek', 'select', 'self',
        'semaphore', 'send', 'sequence', 'series', 'set-locale', 'set-ref-all',
        'set-ref', 'set', 'setf',  'setq', 'sgn', 'share', 'signal', 'silent',
        'sin', 'sinh', 'sleep', 'slice', 'sort', 'source', 'spawn', 'sqrt',
        'starts-with', 'string?', 'string', 'sub', 'swap', 'sym', 'symbol?',
        'symbols', 'sync', 'sys-error', 'sys-info', 'tan', 'tanh', 'term',
        'throw-error', 'throw', 'time-of-day', 'time', 'timer', 'title-case',
        'trace-highlight', 'trace', 'transpose', 'Tree', 'trim', 'true?',
        'true', 'unicode', 'unify', 'unique', 'unless', 'unpack', 'until',
        'upper-case', 'utf8', 'utf8len', 'uuid', 'wait-pid', 'when', 'while',
        'write', 'write-char', 'write-file', 'write-line',
        'xfer-event', 'xml-error', 'xml-parse', 'xml-type-tags', 'zero?',
    )

    # valid names
    valid_name = r'([\w!$%&*+.,/<=>?@^~|-])+|(\[.*?\])+'

    tokens = {
        'root': [
            # shebang
            (r'#!(.*?)$', Comment.Preproc),
            # comments starting with semicolon
            (r';.*$', Comment.Single),
            # comments starting with #
            (r'#.*$', Comment.Single),

            # whitespace
            (r'\s+', Text),

            # strings, symbols and characters
            (r'"(\\\\|\\"|[^"])*"', String),

            # braces
            (r'\{', String, "bracestring"),

            # [text] ... [/text] delimited strings
            (r'\[text\]*', String, "tagstring"),

            # 'special' operators...
            (r"('|:)", Operator),

            # highlight the builtins
            (words(builtins, suffix=r'\b'),
             Keyword),

            # the remaining functions
            (r'(?<=\()' + valid_name, Name.Variable),

            # the remaining variables
            (valid_name, String.Symbol),

            # parentheses
            (r'(\(|\))', Punctuation),
        ],

        # braced strings...
        'bracestring': [
            (r'\{', String, "#push"),
            (r'\}', String, "#pop"),
            ('[^{}]+', String),
        ],

        # tagged [text]...[/text] delimited strings...
        'tagstring': [
            (r'(?s)(.*?)(\[/text\])', String, '#pop'),
        ],
    }
