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
]).config(function($stateProvider, $urlRouterProvider) {
    $stateProvider
        .state("index", {
            url: "/index",
            templateUrl: "{{ angular_template('index.html') }}",
            controller: "IndexController"
        })
    $urlRouterProvider.otherwise("index");

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

        $http.get("{{ settings.absurl("/api/index") }}").success(function(data, status, headers, config) {
            controller.books = data;
        }).
            error(function(data, status, headers, config) {
                console.log(data);
            });

        this.showModal = function(book){
            this.currentBook = book;
            $('#myModal').foundation('reveal', 'open');
        };
    });
