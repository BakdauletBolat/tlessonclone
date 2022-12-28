def users_requests(request):
    data = []
    if request.user.is_authenticated:
        data = request.user.to_requests.all().filter(is_confirmed=False)

    return {"user_requests": data}
