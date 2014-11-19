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
    "ngAnimate",
    "LocalStorageModule",
    'angular-loading-bar',
    "vr.directives.nlForm"
]).config(function($stateProvider, $urlRouterProvider) {
    $stateProvider
        .state("featured", {
            url: "/featured",
            templateUrl: "{{ angular_template('index.html') }}",
            controller: "IndexController"
        })
    $urlRouterProvider.otherwise("featured");

}).config(['cfpLoadingBarProvider', function(cfpLoadingBarProvider) {
    cfpLoadingBarProvider.includeSpinner = true;
    cfpLoadingBarProvider.includeBar = true;
}]).run(function($rootScope, $state, $templateCache, $http, localStorageService){
    $rootScope.bongAuthToken = localStorageService.get("token");
    $rootScope.BASE_URL = "{{ settings.absurl("/") }}"
    $rootScope.$state = $state;
    $rootScope.$on("$viewContentLoaded", function() {
        $templateCache.removeAll();
    });
})
    .controller("BoooksMainCtrl", function($scope, $http){
    })
    .controller("BoooksSearchController", function($scope, $http, cfpLoadingBar){
        var controller = this;
        this.chosenNicheID = 1;
        this.chosenCategoryID = 1;
        this.filterMaxPrice = '100';
        this.filterMaxMinutes = '900';
        this.loading = true;

        cfpLoadingBar.start();
        this.applyFilters = function(){
            controller.filteredBooks = [];
            controller.loading = true;
            $http.post("{{ settings.absurl('/api/search') }}", {niche_id: controller.chosenNicheID, category_id: controller.chosenCategoryID, max_price: controller.filterMaxPrice, max_pages: controller.filterMaxMinutes}).
            success(function(data, status, headers, config) {
                console.log("data: ", data);
                controller.books = data;
                controller.filteredBooks = data;
                controller.loading = false;
            }).
            error(function(data, status, headers, config) {
                console.log(data);
                controller.loading = false;
                controller.filteredBooks = false;
            });
        };

        this.showModal = function(book){
            this.currentBook = book;
            $('#myModal').foundation('reveal', 'open');
        };

        $http.get("{{ settings.absurl("/api/index") }}").success(function(data, status, headers, config) {
            console.log("data: ", data);
            controller.books = data;
                controller.loading = false;
            controller.filteredBooks = data;
        }).
        error(function(data, status, headers, config) {
                controller.loading = false;
            controller.filteredBooks = false;
        });

    });
