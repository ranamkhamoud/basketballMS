from .utils import is_player, is_coach, is_manager

def user_roles(request):
    return {
        'is_player': is_player(request.user),
        'is_coach': is_coach(request.user),
        'is_manager': is_manager(request.user),
    }
