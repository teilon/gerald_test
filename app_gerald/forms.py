from django import forms


class FinderForm(forms.Form):

    text = forms.CharField(max_length=40,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'hello',
                                      'aria-label': 'gerald', 'aria-describedby': 'add-btn'}))
