from django import template

register = template.Library()


@register.filter(name='check')
def check(user, user_2):
    for item in user.subscriptions.all():
        if item.id == user_2.id:
            for item_2 in user_2.subscriptions.all():
                if item_2.id == user.id:
                    return 'Вы друзья'
            return 'Вы уже отправили запрос'
    return 'Добавить в друзья'
