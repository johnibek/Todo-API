from rest_framework import serializers
from .models import Todo, CustomUser

class ToDoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    datetime = serializers.SerializerMethodField(method_name='get_datetime')
    class Meta:
        model = Todo
        fields = ['id', 'user', 'body', 'done', 'datetime']

    def get_datetime(self, todo_item: Todo):
        return todo_item.datetime.strftime("%d-%m-%Y %I:%M:%S")
