import sys

if sys.version_info < (3, 7):
    from ._tickformatstop import Tickformatstop
    from ._tickfont import Tickfont
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__, [], ["._tickformatstop.Tickformatstop", "._tickfont.Tickfont"]
    )
