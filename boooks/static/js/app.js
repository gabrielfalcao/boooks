angular.module("BoooksApp", [
    "ui.router",
    "LocalStorageModule",
    "BoooksApp.Common",
    "BoooksApp.Auth",
    "BoooksApp.Index",
]).config(function($stateProvider, $urlRouterProvider) {
    $stateProvider
        .state("index", {
            url: "/index",
            templateUrl: "{{ angular_template('index.html') }}",
            controller: "IndexController"
        })
        .state("login", {
            url: "/login",
            templateUrl: "{{ angular_template('login.html') }}",
            controller: "LoginController"
        })
        .state("not-found", {
            url: "/not-found",
            templateUrl: "{{ angular_template('404.html') }}"
        });
    $urlRouterProvider.otherwise("index");

}).run(function($rootScope, $state, $templateCache, $http, localStorageService){
    $rootScope.boooksAuthToken = localStorageService.get("token");
    $rootScope.BASE_URL = "{{ settings.absurl("/") }}"
    $rootScope.$state = $state;
    $rootScope.$on("$viewContentLoaded", function() {
        $templateCache.removeAll();
    });
    $rootScope.isAuthenticated = function(){
        var validtoken =  (typeof $rootScope.boooksAuthToken === 'string') && ($rootScope.boooksAuthToken.length > 0);
        if (validtoken) {
            return true;
        }
        $state.go("login");
    };
})
.controller("BoooksMainCtrl", function($scope, $http){
});
