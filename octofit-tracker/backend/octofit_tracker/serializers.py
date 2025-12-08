from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if 'id' in rep:
            rep['id'] = str(rep['id'])
        return rep

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if 'id' in rep:
            rep['id'] = str(rep['id'])
        return rep

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if 'id' in rep:
            rep['id'] = str(rep['id'])
        return rep

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if 'id' in rep:
            rep['id'] = str(rep['id'])
        return rep

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if 'id' in rep:
            rep['id'] = str(rep['id'])
        return rep
