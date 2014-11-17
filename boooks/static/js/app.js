var app = (function(document, $) {

    'use strict';
    var docElem = document.documentElement,

    _userAgentInit = function() {
	docElem.setAttribute('data-useragent', navigator.userAgent);
    },
    _init = function() {
	$(document).foundation();
	_userAgentInit();
    };

    return {
	init: _init
    };

})(document, jQuery);

(function() {

    'use strict';
    app.init();

})();

angular.module("BoooksApp", [
    "ui.router",
    "LocalStorageModule",
    "vr.directives.nlForm"
]).config(function($stateProvider, $urlRouterProvider) {
    $stateProvider
        .state("featured", {
            url: "/featured",
            templateUrl: "{{ angular_template('index.html') }}",
            controller: "IndexController"
        })
    $urlRouterProvider.otherwise("featured");

}).run(function($rootScope, $state, $templateCache, $http, localStorageService){
    $rootScope.bongAuthToken = localStorageService.get("token");
    $rootScope.BASE_URL = "{{ settings.absurl("/") }}"
    $rootScope.$state = $state;
    $rootScope.$on("$viewContentLoaded", function() {
        $templateCache.removeAll();
    });
})
    .controller("BoooksMainCtrl", function($scope, $http){
    })
    .controller("BoooksSearchController", function($scope, $http){
        var controller = this;
        this.filterKind = 'popular';
        this.filterAbout = 'art & design';
        this.applyFilters = function(){
            $http.post("{{ settings.absurl('/api/search') }}", {keywords: [controller.filterKind, controller.filterAbout].join(' ')}).
            success(function(data, status, headers, config) {
                console.log("data: ", data);
                controller.books = data;
                controller.filteredBooks = data;
            }).
            error(function(data, status, headers, config) {
                console.log(data);
            });
        };

        this.showModal = function(book){
            this.currentBook = book;
            $('#myModal').foundation('reveal', 'open');
        };

        $http.get("{{ settings.absurl("/api/index") }}").success(function(data, status, headers, config) {
            console.log("data: ", data);
            controller.books = data;
            controller.filteredBooks = data;
        }).
        error(function(data, status, headers, config) {
            console.log("error: ", data);
        });

    });
