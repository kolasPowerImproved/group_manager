from rest_framework import serializers
from base.models import Child, Group, Trainer, ImagesForSlider, GroupMusic


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = (
            "first_name",
            "second_name",
            "last_name",
            "date_of_birth",
            "child_phone_number",
            "parents_phone_number",
            "groups",
            "gender",
            "parents_name",
            "payment",
            "date_of_payment"
        )

    def create(self, validated_data):
        """
        Create new child with several fields
        :param validated_data:
        :return:
        """
        return Child.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Child' instance, give the validated data
        :param instance:
        :param validated_data:
        :return:
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.second_name = validated_data.get('second_name', instance.second_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.child_phone_number = validated_data.get('child_phone_number', instance.child_phone_number)
        instance.parents_phone_number = validated_data.get('parents_phone_number', instance.parents_phone_number)
        instance.groups = validated_data.get('groups', instance.groups)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.parents_name = validated_data.get('parents_name', instance.parents_name)
        instance.payment = validated_data.get('payment', instance.payment)
        instance.date_of_payment = validated_data.get('date_of_payment', instance.date_of_payment)
        instance.save()
        return instance


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = (
            "first_name",
            "second_name",
            "last_name",
            "trainer_phone_number"
        )

    def create(self, validated_data):
        """
        Create and return new 'Trainer'
        :param validated_data:
        :return:
        """
        return Trainer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Trainer' instatnce, give the validated data
        :param instance:
        :param validated_data:
        :return:
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.second_name = validated_data.get('second_name', instance.second_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.trainer_phone_number = validated_data.get('trainer_phone_number', instance.trainer_phone_number)
        instance.save()
        return instance


class ImagesForSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesForSlider
        fields = (
            "image",
            "image_name",
            'id',
        )


class GroupMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMusic
        fields = (
            "music",
            "music_name",
            'id',
        )


class GroupSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer()
    images_for_slider = ImagesForSliderSerializer(many=True)
    music_for_player = GroupMusicSerializer(many=True)

    class Meta:
        model = Group
        fields = (
            "group_name",
            "group_description",
            "group_image",
            "group_music",
            "salary",
            'trainer',
            'monday_time',
            'tuesday_time',
            'wednesday_time',
            'thursday_time',
            'friday_time',
            'saturday_time',
            'sunday_time',
            'images_for_slider',
            'music_for_player',
        )

    def create(self, validated_data):
        """
        Create and return new 'Group'
        :param validated_data:
        :return:
        """
        return Group.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Group' instance, give the validated data
        :param instance:
        :param validated_data:
        :return:
        """
        instance.group_name = validated_data.get('group_name', instance.group_name)
        instance.group_description = validated_data.get('group_description', instance.group_description)
        instance.group_image = validated_data.get('group_image', instance.group_image)
        instance.images_for_slider = validated_data.get('images_for_slider', instance.images_for_slider)
        instance.group_music = validated_data.get('group_music', instance.group_music)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.trainer = validated_data.get('trainer', instance.trainer)
        instance.save()
        return instance



