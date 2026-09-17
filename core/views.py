from django.shortcuts import render


# =====================================================
# HOME
# =====================================================

def home(request):

    products = [
        {
            "name": "Red Invite Card with Bride And Groom Names",
            "price": "10.25",
            "image": "images/exclusive-hindu.jpg",
        },
        {
            "name": "Simple Red and Yellow Card Invite",
            "price": "5.00",
            "image": "images/exclusive-luxury.jpg",
        },
        {
            "name": "Red Vertical Personal Invite",
            "price": "7.00",
            "image": "images/exclusive-floral.jpg",
        },
        {
            "name": "Floral Personal Wedding Invite",
            "price": "7.50",
            "image": "images/theme-birds.jpg",
        },
        {
            "name": "Elegant Brown Wedding Invite",
            "price": "7.00",
            "image": "images/theme-palace.jpg",
        },
        {
            "name": "Maroon Traditional Wedding Card",
            "price": "9.00",
            "image": "images/theme-beach.jpg",
        },
    ]

    return render(
        request,
        "core/home.html",
        {
            "products": products,
        },
    )


# =====================================================
# LOGIN
# =====================================================

def login(request):

    return render(
        request,
        "accounts/login.html"
    )


# =====================================================
# WEDDING INVITATIONS
# =====================================================

def wedding_invitations(request):

    return render(
        request,
        "products/wedding_invitations.html"
    )


# =====================================================
# SPECIAL OCCASIONS
# =====================================================

def special_occasions(request):

    return render(
        request,
        "products/special_occasions.html"
    )


# =====================================================
# THEME CARDS
# =====================================================

def theme_cards(request):

    return render(
        request,
        "products/theme_cards.html"
    )


# =====================================================
# SCROLL INVITATIONS
# =====================================================

def scroll_invitations(request):

    return render(
        request,
        "products/scroll_invitations.html"
    )


# =====================================================
# DIGITAL INVITATIONS
# =====================================================

def digital_invitations(request):

    return render(
        request,
        "products/digital_invitations.html"
    )


# =====================================================
# WISHLIST
# =====================================================

def wishlist(request):

    return render(
        request,
        "wishlist/wishlist.html"
    )

def cart(request):
    return render(
        request,
        "cart/cart.html"
    )

# =====================================================
# PLACEHOLDER
# =====================================================

def placeholder(request):

    return render(
        request,
        "core/placeholder.html"
    )