from django imort fomrs
from blog.models import Post,Comment

class PoseForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = { # specified css class name
            'title':foms.TextInput(attrs={'class':'textinputclass'}),
            'text':froms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':foms.TextInput(attrs={'class':'textinputclass'}),
            'text':froms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
