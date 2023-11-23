from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Row, Column, Field, Submit
from django import forms


class FilterByLetterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "get"
        self.helper.form_class = "form-inline"
        self.helper.layout = Layout(
            Div(
                Div(
                    Field("last_name", wrapper_class="col-md-1"),
                    css_class="row",
                ),
                Div(
                    Field("initial_letter", wrapper_class="col-md-1"),
                    css_class="row",
                ),
                css_class="form-row",
            ),
        )
