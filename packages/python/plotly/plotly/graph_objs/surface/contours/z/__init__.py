import sys

if sys.version_info < (3, 7):
    from ._project import Project
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(__name__, [], ["._project.Project"])
