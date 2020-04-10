import sys

if sys.version_info < (3, 7):
    from ._width import WidthValidator
    from ._visible import VisibleValidator
    from ._valueminus import ValueminusValidator
    from ._value import ValueValidator
    from ._type import TypeValidator
    from ._tracerefminus import TracerefminusValidator
    from ._traceref import TracerefValidator
    from ._thickness import ThicknessValidator
    from ._symmetric import SymmetricValidator
    from ._copy_zstyle import Copy_ZstyleValidator
    from ._color import ColorValidator
    from ._arraysrc import ArraysrcValidator
    from ._arrayminussrc import ArrayminussrcValidator
    from ._arrayminus import ArrayminusValidator
    from ._array import ArrayValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [],
        [
            "._width.WidthValidator",
            "._visible.VisibleValidator",
            "._valueminus.ValueminusValidator",
            "._value.ValueValidator",
            "._type.TypeValidator",
            "._tracerefminus.TracerefminusValidator",
            "._traceref.TracerefValidator",
            "._thickness.ThicknessValidator",
            "._symmetric.SymmetricValidator",
            "._copy_zstyle.Copy_ZstyleValidator",
            "._color.ColorValidator",
            "._arraysrc.ArraysrcValidator",
            "._arrayminussrc.ArrayminussrcValidator",
            "._arrayminus.ArrayminusValidator",
            "._array.ArrayValidator",
        ],
    )
