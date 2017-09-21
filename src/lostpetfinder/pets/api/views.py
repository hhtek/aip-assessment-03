from django.db.models import Q # filter using operators '&' or '|'

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)

from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
)

# Custom permissions
from .permissions import IsOwnerOrReadOnly

from .serializers import (
    PetListSerializer,
    PetDetailSerializer,
    PetCreateUpdateSerializer,
)

from pets.models import Pet

class PetListAPIView(ListAPIView):
    """
    Get all pets
    """
    serializer_class = PetListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['status', 'name', 'location', 'pet_type']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Pet.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(status__icontains=query)|
                Q(name__icontains=query)|
                Q(location__icontains=query)|
                Q(pet_type__icontains=query)
            ).distinct()
        return queryset_list

class PetDetailAPIView(RetrieveAPIView):
    """
    Get specific pet details.
    """
    queryset = pets = Pet.objects.all()
    serializer_class = PetDetailSerializer
    lookup_field = 'slug'

class PetCreateAPIView(CreateAPIView):
    """
    Create a pet.
    """
    queryset = pets = Pet.objects.all()
    serializer_class = PetCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PetRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """
    Update specific pet.
    """
    queryset = pets = Pet.objects.all()
    serializer_class = PetCreateUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class PetDeleteAPIView(DestroyAPIView):
    """
    Delete specific pet.
    """
    queryset = pets = Pet.objects.all()
    serializer_class = PetDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'slug'
