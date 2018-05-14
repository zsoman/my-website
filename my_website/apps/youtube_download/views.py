from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import YoutubeVideo, YoutubePlaylist
from .serializers import YoutubeVideoSerializer, YoutubePlaylistSerializer


class YoutubeVideoViewSet(ModelViewSet):
    queryset = YoutubeVideo.objects.all()
    serializer_class = YoutubeVideoSerializer
    # authentication_classes = (JSONWebTokenAuthentication,)


class YoutubePlaylistViewSet(ModelViewSet):
    queryset = YoutubePlaylist.objects.all()
    serializer_class = YoutubePlaylistSerializer
    # authentication_classes = (JSONWebTokenAuthentication,)

    # @detail_route(methods=['post'])
    # def join(self, request, pk):
    #     user_group = self.get_object()
    #
    #     if user_group.state == UserGroupStates.CLOSED:
    #         raise ClosedGroupException('{} group is closed group'.format(user_group))
    #     try:
    #         membership = request.user.memberships.get(group=user_group)
    #     except Membership.DoesNotExist:
    #         Membership.objects.create(user=request.user, group=user_group)
    #     else:
    #         if membership.type == MembershipTypes.BANNED:
    #             raise BanUserException('{} user is banned from {} group'.format(request.user, user_group))
    #         elif membership.type == MembershipTypes.NOT_MEMBER:
    #             membership.type = MembershipTypes.MEMBER
    #             membership.save()
    #     return Response(self.serializer_class(user_group).data)
    #
    # @detail_route(methods=['post'])
    # def join_request(self, request, pk):
    #     user_group = self.get_object()
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     if user_group.state == UserGroupStates.CLOSED:
    #         serializer.save()
    #         return Response(serializer.data)
    #     raise JoinRequestException("Can't create join request for {} group".format(user_group))
    #
    # @detail_route(methods=['post'])
    # def leave(self, request, pk):
    #     user_group = self.get_object()
    #     membership = request.user.memberships.get(group=user_group)
    #     if len(Membership.objects.filter(group=user_group,
    #                                      type=MembershipTypes.ADMIN)) == NUMBER_OF_MINIMUM_ADMINS_IN_USER_GROUP and \
    #             membership.type == MembershipTypes.ADMIN:
    #         raise LeaveGroupException(
    #             '{} group has to have at least one admin, {} is the last admin'.format(user_group, request.user))
    #     if membership.type != MembershipTypes.BANNED:
    #         membership.type = MembershipTypes.NOT_MEMBER
    #         membership.save()
    #     return Response(self.serializer_class(user_group).data)
    #
    # @detail_route(methods=['post'])
    # def ban(self, request, pk):
    #     user_group = self.get_object()
    #     serializer = MembershipSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     if Membership.objects.filter(group=user_group, user=request.user, type=MembershipTypes.ADMIN).exists():
    #         membership = Membership.objects.get(user=serializer.validated_data['user'],
    #                                             group=serializer.validated_data['group'])
    #         if membership.type == MembershipTypes.ADMIN:
    #             raise BanUserException(
    #                 "{} user is admin of {} group, can't ban admin".format(membership.user, user_group))
    #         membership.type = MembershipTypes.BANNED
    #         membership.save()
    #         return Response(self.serializer_class(user_group).data)
    #     raise NotAdminException(
    #         "{} user is not admin of {} group, only admins can ban users".format(request.user, user_group))
    #
    # def get_serializer_context(self):
    #     context = super(UserGroupViewSet, self).get_serializer_context()
    #     if self.action == 'join_request':
    #         context['group'] = self.get_object()
    #     return context
    #
    # def get_serializer_class(self):
    #     if self.action == 'join_request':
    #         return UserGroupJoinRequestSerializer
    #     return self.serializer_class
