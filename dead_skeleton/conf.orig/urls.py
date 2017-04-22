from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings

# from dead_users.views import signup

urlpatterns = [
    # admin
    url(r'^admin/', admin.site.urls),

    # salmonella
    url(r'^admin/salmonella/', include('salmonella.urls')),

    # captcha
    url(r'^captcha/', include('captcha.urls')),

    # smart_selects
    url(r'^chaining/', include('smart_selects.urls')),

    # all auth
    # url(r"^accounts/signup/$", signup, name="account_signup"),
    url(r'^accounts/', include('allauth.urls')),

    # dead tests
    url(r'^dead/tests$', TemplateView.as_view(template_name="dead-common/home-tests.html"), name='dead-tests'),

    # dead js utilities
    url(r'^dead/js/tests/', include('dead_js_utilities.urls', namespace='dead-js-utilities')),

    # dead forms
    url(r'^dead/forms/tests/', include('dead_forms.urls', namespace='dead-forms')),

    # home
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
]

# media
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

# admin title
if settings.SHOW_ADMIN_TITLE:
    admin.site.site_header = settings.ADMIN_TITLE

# handler400 = 'applications.common.views.bad_request'
# handler500 = 'applications.common.views.server_error'
