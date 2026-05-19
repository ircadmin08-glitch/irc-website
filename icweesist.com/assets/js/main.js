/*===================================================
    Template Scripts
====================================================*/
(function ($) {
    "use strict";

    // Preloader
    $(window).on('load', function () {
        $('body').addClass('loaded');
    });

    $(document).ready(function () {

        var html = $('html');

        // Responsive Classes
        function responsiveClasses() {
            var body = $("body");
            if ($(window).width() < 992) {
                body.removeClass("viewport-lg");
                body.addClass("viewport-sm");
            } else {
                body.removeClass("viewport-sm");
                body.addClass("viewport-lg");
            }
        }

        // Window Resize
        $(window).on("resize", function () {
            responsiveClasses();
        }).resize();

        // Sticky Header
        function stickyHeader() {
            var mainHeader = $(".main-header"),
                headerClone = mainHeader.clone();
            mainHeader.after('<div class="sticky-header"></div>');
            $(".sticky-header").html(headerClone);

            var headerSelector = document.querySelector(".sticky-header"),
                triggerPoint = mainHeader.height(),
                yOffset = 0;

            $(window).on("scroll", function () {
                yOffset = $(window).scrollTop();
                if (yOffset >= triggerPoint) {
                    $(".sticky-header").addClass("sticky-fixed-top");
                } else {
                    $(".sticky-header").removeClass("sticky-fixed-top");
                }
            });
        }

        if ($(window).width() > 992) {
            stickyHeader();
        }

        // Mobile Menu
        function mobileMenu() {
            $("header.main-header").after('<div class="mobile-navigation-menu"><button id="mobile-menu-close"><i class="la la-close"></i></button></div>');
            var menuWrapper = $("header.main-header .header-menu-wrap .nav-menu").clone();
            $('.mobile-navigation-menu #mobile-menu-close').after(menuWrapper);

            $("#mobile-menu-close, .mobile-menu-icon").on("click", function () {
                $(".mobile-menu-icon").toggleClass("menu-open");
                $(".mobile-navigation-menu").toggleClass("open-mobile-menu");
            });

            $(".mobile-navigation-menu ul li:has(ul)").each(function () {
                $(this).append('<span class="dropdown-plus"></span>');
                $(this).addClass("dropdown_menu");
            });

            $(".mobile-navigation-menu .dropdown-plus").on("click", function () {
                $(this).prev("ul").slideToggle(300);
                $(this).toggleClass("dropdown-open");
                $(".mobile-navigation-menu ul li:has(ul)").toggleClass("dropdown-open");
            });

            $(".mobile-navigation-menu .dropdown_menu a").append("<span></span>");
        }

        mobileMenu();

        // Popup Search Box
        $(function () {
            $("#popup-search-box").removeClass("toggled");
            $("body").removeClass("open-search-box");
            $(".dl-search-icon").on("click", function (e) {
                e.stopPropagation();
                $("body").toggleClass("open-search-box");
                $("#popup-search").focus();
            });

            $("#popup-search-box input").on("click", function (e) {
                e.stopPropagation();
            });
            $(document).on(
                "click",
                ".search-close, #searchbox-overlay",
                function (e) {
                    e.preventDefault();
                    $("body.open-search-box").removeClass("open-search-box");
                }
            );
        });

        

        // Accordion
        $('.faq-accordion .accordion-item').on('click', function () {
            $(".faq-accordion .accordion-item.active").removeClass("active");
            if (!$('.faq-accordion .accordion-item').hasClass('active')) {
                $(this).addClass("active");
            }
            return false;
        });

        // Funfact Counter
        $('.counter-item').waypoint(
            function () {
                var odo = $(".counter-item .odometer");
                odo.each(function () {
                    var countNumber = $(this).attr("data-count");
                    $(this).html(countNumber);
                });
            }, {
                offset: "80%",
                triggerOnce: true
            }
        );

        // Wow JS Active
        new WOW().init();

        // Nice Select Active
        $('select').niceSelect();

        // Current Year
        var currentYear = new Date().getFullYear();
        $('#currentYear').append(currentYear);

        // Scrool To Top
        var scrollTop = $("#scroll-top");
        $(window).on('scroll', function () {
            var topPos = $(this).scrollTop();
            if (topPos > 100) {
                $('#scrollup').removeClass('hide');
                $('#scrollup').addClass('show');

            } else {
                $('#scrollup').removeClass('show');
                $('#scrollup').addClass('hide');
            }
        });

        $(scrollTop).on("click", function () {
            $('html, body').animate({
                scrollTop: 0
            }, 100);
            return false;
        });

        // Custom Cursor
        function customCursor() {
            $('body').append('<div class="dl-cursor"></div>');
            var cursor = $('.dl-cursor'),
                projectView = $('.project-view');

            $(window).on('mousemove', function (e) {
                cursor.css({
                    'transform': 'translate(' + (e.clientX - 5) + 'px,' + (e.clientY - 5) + 'px)',
                    'visibility': 'inherit'
                });
            });

            $(window).on('mouseout', function () {
                cursor.css('visibility', 'hidden');
            });
            projectView.each(function () {
                $(this).on('mouseleave', function () {
                    cursor.removeClass('expand');
                });
                $(this).on('mouseover', function () {
                    cursor.addClass('expand');
                });
            });
        }

        if ($('body').hasClass('viewport-lg')) {
            customCursor();
        }

        // Venobox Active
        $('.venobox').venobox({
            bgcolor: 'transparent',
            spinner: 'spinner-pulse',
            numeration: true,
            infinigall: true
        });

    });

})(jQuery);
