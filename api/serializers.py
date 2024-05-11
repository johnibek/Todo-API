from rest_framework import serializers
from .models import Todo, CustomUser, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ToDoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    datetime = serializers.SerializerMethodField(method_name='get_datetime')

    class Meta:
        model = Todo
        fields = ['id', 'user', 'body', 'done', 'datetime', 'category', 'category_id']

    def get_datetime(self, todo_item: Todo):
        return todo_item.datetime.strftime("%d-%m-%Y %H:%M:%S %p")
