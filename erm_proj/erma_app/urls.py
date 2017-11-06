from django.conf.urls import url
from erma_app import views

# for URL template
app_name = 'erma_app'

urlpatterns = [
    url(r'^form/',views.form_name_view,name='form_name'),
    url(r'^regiser/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
