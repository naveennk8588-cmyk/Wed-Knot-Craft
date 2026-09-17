from django.urls import path
from . import views


urlpatterns = [

    # =====================================================
    # HOME
    # =====================================================

    path(
        "",
        views.home,
        name="home"
    ),


    # =====================================================
    # WEDDING INVITATIONS
    # =====================================================

    path(
        "wedding-invitations/",
        views.wedding_invitations,
        name="wedding_invitations"
    ),


    # =====================================================
    # SPECIAL OCCASIONS
    # =====================================================

    path(
        "special-occasions/",
        views.special_occasions,
        name="special_occasions"
    ),


    # =====================================================
    # THEME CARDS
    # =====================================================

    path(
        "theme-cards/",
        views.theme_cards,
        name="theme_cards"
    ),


    # =====================================================
    # SCROLL INVITATIONS
    # =====================================================

    path(
        "scroll-invitations/",
        views.scroll_invitations,
        name="scroll_invitations"
    ),


    # =====================================================
    # DIGITAL INVITATIONS
    # =====================================================

    path(
        "digital-invitations/",
        views.digital_invitations,
        name="digital_invitations"
    ),


    # =====================================================
    # LOGIN
    # =====================================================

    path(
        "login/",
        views.login,
        name="login"
    ),


    # =====================================================
    # WISHLIST
    # =====================================================

   path(
    "wishlist/",
    views.wishlist,
    name="wishlist"
),


    # =====================================================
    # CART
    # =====================================================

    path(
    "cart/",
    views.cart,
    name="cart"
),


    # =====================================================
    # SEARCH
    # =====================================================

    path(
        "search/",
        views.placeholder,
        name="product_search"
    ),


    # =====================================================
    # ABOUT
    # =====================================================

    path(
        "about/",
        views.placeholder,
        name="about"
    ),


    # =====================================================
    # CONTACT
    # =====================================================

    path(
        "contact/",
        views.placeholder,
        name="contact"
    ),


    # =====================================================
    # FAQ
    # =====================================================

    path(
        "faq/",
        views.placeholder,
        name="faq"
    ),

]