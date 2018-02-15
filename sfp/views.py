from django.template.loader import TemplateDoesNotExist
from django.http import Http404
from django.shortcuts import render
from django.conf import settings


HANDLE_HOMEPAGE = getattr(settings, "SFP_HANDLE_HOMEPAGE", False)


def staticflatpage(request, path):
    global HANDLE_HOMEPAGE
    """Load/render a template corresponding to the path (a URL)"""
    # Don't render a base.html template.
    if path.replace("/", '').lower() == "base":
        raise Http404

    if not path.startswith('/'):
        path = "/{0}".format(path)
    if path.endswith('/'):
        path = path[:-1]

    # paths should be in the format: sfp/path/from/url.html
    template_path = "pages{0}.html".format(path)
    if HANDLE_HOMEPAGE is True:
        if path == "":
            template_path = "pages/index.html"
    try:
        return render(request, template_path)
    except TemplateDoesNotExist:
        raise Http404
