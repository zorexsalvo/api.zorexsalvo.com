from django_markup.markup import formatter
from rest_framework.serializers import ModelSerializer
from .models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        data = super(PostSerializer, self).to_representation(instance)
        data.update(
            {
                'content': formatter(
                    instance.content, filter_name='linebreaks'
                )
            }
        )
        return data
