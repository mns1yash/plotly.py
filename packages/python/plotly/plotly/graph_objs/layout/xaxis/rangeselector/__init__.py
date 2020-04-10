import sys

if sys.version_info < (3, 7):
    from ._font import Font
    from ._button import Button
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__, [], ["._font.Font", "._button.Button"]
    )
