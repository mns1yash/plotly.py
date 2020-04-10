import _plotly_utils.basevalidators


class LatsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="latsrc", parent_name="densitymapbox", **kwargs):
        super(LatsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
