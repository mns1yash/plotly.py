import sys

if sys.version_info < (3, 7):
    from ._widthsrc import WidthsrcValidator
    from ._width import WidthValidator
    from ._colorsrc import ColorsrcValidator
    from ._color import ColorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [],
        [
            "._widthsrc.WidthsrcValidator",
            "._width.WidthValidator",
            "._colorsrc.ColorsrcValidator",
            "._color.ColorValidator",
        ],
    )
