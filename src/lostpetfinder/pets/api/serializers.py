from rest_framework.serializers import ModelSerializer

from pets.models import Pet

class PetListSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = [
            'slug',
            'owner',
            'name',
            'location',
            'pet_type',
            'colour',
            'age',
            'size',
            'gender',
            'desexed',
            'collar',
            'microchipped',
            'microchipped_no',
            'missing_date',
            'status',
            'description',
            'pet_image',
            'timestamp',
            'updated',
        ]

class PetDetailSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = [
            'slug',
            'owner',
            'name',
            'location',
            'pet_type',
            'colour',
            'age',
            'size',
            'gender',
            'desexed',
            'collar',
            'microchipped',
            'microchipped_no',
            'missing_date',
            'status',
            'description',
            'pet_image',
            'timestamp',
            'updated',
        ]

class PetCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = [
            'id',
            'slug',
            'owner',
            'name',
            'location',
            'pet_type',
            'colour',
            'age',
            'size',
            'gender',
            'desexed',
            'collar',
            'microchipped',
            'microchipped_no',
            'missing_date',
            'status',
            'description',
            'pet_image',
        ]
