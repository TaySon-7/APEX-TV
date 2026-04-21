from rest_framework import serializers
from movie.domain.models import Genre
from movie.domain.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("название жанра должно содержать минимум 4 символа")
        return value.strip()

    def validate_slug(self, value):
        if ' ' in value:
            raise serializers.ValidationError("slug не должен содержать пробелы")
        return value
