from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),
    path('reservation/', views.reservation, name='reservation'),
    path('faq/', views.faq, name='faq'),
    path('tours/', views.tours, name='tours'),
    path('tours-details/<int:pk>/', views.tours_details, name='tours_details'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='registration'),
    path('logout-user/', views.logout_view, name='logout-user'),
    path('invoice/<int:id>/', views.invoice, name='invoice'),
    path('mytour-detail/<int:id>/', views.mytourdetail, name='mytour-detail'),
    path('click_generate_url/<int:amount>/<int:tour_id>/', views.click_generate_url, name='click_generate_url'),
    path('payme_generate_url/<int:amount>/<int:tour_id>/', views.payme_generate_url, name='payme_generate_url'),
    path('success_payment', views.payment_success, name='success_payment')
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
