from django.contrib.auth.models import User, Group
import django_filters
from drf_haystack.viewsets import HaystackViewSet
from rest_framework import viewsets
from rest_framework.decorators import action

from api import models
from api import serializers


class ManifestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Manifest.objects.all()
    serializer_class = serializers.ManifestSerializer

class SearchView(HaystackViewSet):

    # `index_models` is an optional list of which models you would like to include
    # in the search result. You might have several models indexed, and this provides
    # a way to filter out those of no interest for this particular view.
    # (Translates to `SearchQuerySet().models(*index_models)` behind the scenes.
    serializer_class = serializers.AggregateSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer

class DocumentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer
    filter_fields = (
        'slug',
        'title',
        'organization',
        'license',
        )

class SpellFilter(django_filters.FilterSet):
  
    class Meta:
        model = models.Spell
        fields = {
            'slug': ['in', 'iexact', 'exact', 'in', ],
            'name': ['iexact', 'exact'],
            'level': ['iexact', 'exact', 'in', ],
            'level_int': ['iexact', 'exact', 'range'],
            'school': ['iexact', 'exact', 'in', ],
            'duration': ['iexact', 'exact', 'in', ],
            'components': ['iexact', 'exact', 'in', ],
            'concentration': ['iexact', 'exact', 'in', ],
            'casting_time': ['iexact', 'exact', 'in', ],
            'dnd_class': ['iexact', 'exact', 'in', 'icontains'],
            'document__slug': ['iexact', 'exact', 'in', ],
        }


class SpellViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows viewing of spells.
    """
    # For normal queries, use objects.all()
    queryset = models.Spell.objects.all()
    filter_class=SpellFilter
    serializer_class = serializers.SpellSerializer
    search_fields = ['dnd_class', 'name']
    ordering_fields = '__all__'
    ordering=['name']
    filter_fields = (
        'slug',
        'name',
        'level',
        'level_int',
        'school',
        'duration',
        'components',
        'concentration',
        'casting_time',
        'dnd_class',
        'document__slug',
    )

    @action(detail=False)
    def random(self, request):
        """
        API endpoint that allows viewing of spells, but ordered randomly.
        """
        # For randomized queries, used order_by('?')
        randomized_spells = models.Spell.objects.all().order_by('?')

        page = self.paginate_queryset(randomized_spells)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(randomized_spells, many=True)
        return Response(serializer.data)

class MonsterViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows viewing of monsters.
    """
    queryset = models.Monster.objects.all()
    serializer_class = serializers.MonsterSerializer
    ordering_fields = '__all__'
    ordering = ['name']
    filter_fields = (
        'challenge_rating',
        'armor_class',
        'type',
        'name',
        'document',
        'document__slug',
    )
    search_fields = ['name']

class BackgroundViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows viewing of Backgrounds.
    """
    queryset = models.Background.objects.all()
    serializer_class = serializers.BackgroundSerializer
    ordering_fields = '__all__'
    ordering=['name']
    filter_fields=(
        'name',
        'skill_proficiencies',
        'languages',
        'document__slug',
    )
    search_fields = ['name']

class PlaneViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows viewing of Planes.
    """
    queryset = models.Plane.objects.all()
    serializer_class = serializers.PlaneSerializer
    filter_fields=(
        'name',
        'document__slug',
    )

class SectionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows viewing of Sections.
    """
    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerializer
    ordering_fields = '__all__'
    ordering=['name']
    filter_fields=(
        'name',
        'parent',
        'document__slug',
    )

class FeatViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows viewing of Feats.
    """
    queryset = models.Feat.objects.all()
    serializer_class = serializers.FeatSerializer
    filter_fields=('name','prerequisite', 'document__slug',)

class ConditionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows viewing of Backgrounds.
    """
    queryset = models.Condition.objects.all()
    serializer_class = serializers.ConditionSerializer
    filter_fields=(
        'name',
        'document__slug',
    )

class RaceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows viewing of Races and Subraces.
    """
    queryset = models.Race.objects.all()
    serializer_class = serializers.RaceSerializer
    filter_fields=(
        'name',
        'document__slug',
    )

class SubraceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows viewing of Races and Subraces.
    """
    queryset = models.Subrace.objects.all()
    serializer_class = serializers.SubraceSerializer
    filter_fields=(
        'name',
        'document__slug',
    )

class CharClassViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows viewing of Classes and Archetypes.
    """
    queryset = models.CharClass.objects.all()
    serializer_class = serializers.CharClassSerializer
    filter_fields=(
        'name',
        'document__slug',
    )

class ArchetypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows viewing of Archetypes.
    """
    queryset = models.Archetype.objects.all()
    serializer_class = serializers.ArchetypeSerializer
    filter_fields=(
        'name',
        'document__slug',
    )

class MagicItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows viewing of Archetypes.
    """
    queryset = models.MagicItem.objects.all()
    serializer_class = serializers.MagicItemSerializer
    filter_fields=(
        'name',        
        'document__slug',
    )
    search_fields = ['name']

class WeaponViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows viewing of Archetypes.
    """
    queryset = models.Weapon.objects.all()
    serializer_class = serializers.WeaponSerializer
    filter_fields=(
        'name',        
        'document__slug',
    )
    search_fields = ['name']

class ArmorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows viewing of Archetypes.
    """
    queryset = models.Armor.objects.all()
    serializer_class = serializers.ArmorSerializer
    filter_fields=(
        'name',        
        'document__slug',
    )
    search_fields = ['name']
