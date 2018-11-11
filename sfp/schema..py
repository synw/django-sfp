import graphene
from django.conf import settings
from django.utils._os import safe_join


class Page(graphene.ObjectType):
    url = graphene.String()
    title = graphene.String()
    content = graphene.String()


class PageQuery(graphene.ObjectType):
    page = graphene.Field(Page, url=graphene.String())

    def resolve_page(self, info, url):
        if url == "/":
            url = "/index"
        path = "static/pages{0}.html".format(url)
        filepath = safe_join(settings.BASE_DIR, path)
        path404 = safe_join(settings.BASE_DIR, "static/pages/404.html")
        path500 = safe_join(settings.BASE_DIR, "static/pages/500.html")
        try:
            with open(filepath) as f:
                lines = f.readlines()
                title = lines[0].replace("\n", "")
                content = "\n".join(lines[1:])
        except FileNotFoundError:
            with open(path404) as f:
                title = "Page not found"
                content = "\n".join(f.readlines())
        except:
            with open(path500) as f:
                title = "Technical error"
                content = "\n".join(f.readlines())
        return Page(url, title, content)
