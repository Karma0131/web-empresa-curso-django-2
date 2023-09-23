from .models import Link

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    #print(links)
    for link in links:
        ctx[link.key] = link.url
        #print(ctx.keys(), ctx.values())
        print(link.key, ctx[link.key])
    return ctx

