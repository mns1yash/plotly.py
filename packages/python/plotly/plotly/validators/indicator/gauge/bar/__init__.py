import sys

if sys.version_info < (3, 7):
    from ._thickness import ThicknessValidator
    from ._line import LineValidator
    from ._color import ColorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [],
        [
            "._thickness.ThicknessValidator",
            "._line.LineValidator",
            "._color.ColorValidator",
        ],
    )
