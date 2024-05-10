from rest_framework import serializers
from .models import Todo, CustomUser, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ToDoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    datetime = serializers.SerializerMethodField(method_name='get_datetime')

    class Meta:
        model = Todo
        fields = ['id', 'user', 'category', 'body', 'done', 'datetime']

    def get_datetime(self, todo_item: Todo):
        return todo_item.datetime.strftime("%d-%m-%Y %H:%M:%S %p")
