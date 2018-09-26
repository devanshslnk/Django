from rest_framework import serializers

from snippets.models import Snippets

class SnippetSerializer(serializers.Serializer):
	id=serializers.IntegerField(read_only=True)
	title=serializers.CharField(max_length=101,allow_blank=True,default='')
	code=serializers.CharField(max_length=101);
	linenos=serializers.BooleanField(default=True)


	def create(self,validated_data):
		return Snippets.object.create(**validated_data)
	def update(self,instance,validated_data):
		instances.title=validated_data.get('title',instances.title)
		instances.code=validated_data.get('code',instances.code)
		instances.linenos=validates_data.get('linenos',instances.linenos)
		instances.save()
		return instances



# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ('id', 'title', 'code', 'linenos')
