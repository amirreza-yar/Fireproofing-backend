from django.urls import path
from . import views

app_name = 'adminP'
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.login_admin, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("personal/list/", views.personel_list, name="personel_list"),
    path("personel/add/", views.personel_add.as_view(), name="personel_add"),
    path("personel/edit/<int:pk>/", views.Personel_Update.as_view(), name="personel_edit"),
    path("personel/delete/<int:personel>/", views.delete_personel, name="personel_delete"),
    path("user/list/", views.user_list, name="user_list"),
    path("category/", views.Category_view.as_view(), name="category"),
    path("category/<int:pk>/", views.CategoryEdit.as_view(), name="category_edit"),
    path("category/del/<int:pk>/", views.category_delete, name="category_delete"),
    path("weblog/list/", views.weblog_list, name="weblog_list"),
    path("weblog/edit/<int:pk>/", views.weblog_edit.as_view(), name="weblog_edit"),
    path("weblog/add/", views.weblog_add.as_view(), name="weblog_add"),
    path("weblog/delete/<int:pk>/", views.weblog_delete, name="weblog_delete"),
    path("product/list/", views.product_list, name="product_list"),
    path("product/add/", views.product_add.as_view(), name="product_add"),
    path("product/edit/<int:pk>/", views.product_edit.as_view(), name="product_edit"),
    path("product/deleter/<int:pk>/", views.product_delete, name="product_delete"),
    path("order/list/", views.order_list, name="order_list"),
    path("order/deatil/<int:pk>/", views.order_detail, name="order_detail"),
    path("order/cancel/<int:pk>/", views.order_cancel, name="order_cancel"),
    path("order/set-status/<int:pk>/<slug:status>", views.order_set_status, name="set_status"),
]