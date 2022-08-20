from django.urls import path

from . import views

app_name = "product"

urlpatterns = [
    path('',views.product_list,name="product_list"),
    path('<int:id>',views.product_detail, name ="product_detail"),
    path('update/<int:id>',views.product_update, name ="product_update"),
    path('updatecomment/<int:id>',views.comment_update, name ="comment_update"),
    path("category/<slug:category>",views.Product_Category,name="category"),
    path("tag/<slug:tag>",views.Product_Tag,name="tag"),
    path("search/",views.search,name="search"),
]