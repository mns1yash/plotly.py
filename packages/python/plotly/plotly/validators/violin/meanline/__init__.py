import sys

if sys.version_info < (3, 7):
    from ._width import WidthValidator
    from ._visible import VisibleValidator
    from ._color import ColorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [],
        [
            "._width.WidthValidator",
            "._visible.VisibleValidator",
            "._color.ColorValidator",
        ],
    )
