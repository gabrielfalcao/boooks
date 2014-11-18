angular.module("AdminApp", [
    "ui.router",
    "LocalStorageModule",
    "vr.directives.nlForm"
]).config(function($stateProvider, $urlRouterProvider) {
    $stateProvider.state("featured", {
        url: "/admin",
        templateUrl: "{{ angular_template('admin.html') }}",
        controller: "AdminController"
    });
    $urlRouterProvider.otherwise("featured");
}).run(function($rootScope, $state, $templateCache, $http, localStorageService){
    $rootScope.BASE_URL = "{{ settings.absurl("/") }}"
    $rootScope.$state = $state;
    $rootScope.$on("$viewContentLoaded", function() {
        $templateCache.removeAll();
    });
}).controller("AdminMainCtrl", function($scope, $http){
}).controller("AdminController", function($scope, $http){
    var controller = this;
    controller.categories = [];
    controller.niches = [];
    controller.keywords = [];

    this.saveKeywords = function(keywords) {
        $http.post("/api/keywords", {keywords: keywords}).success(function(data, status, headers, config) {

        }).error(function(data, status, headers, config) {
            console.log(data)
        });
    };

    this.updateNiches = function() {
        $http.get("{{ settings.absurl("/api/niches") }}").success(function(data, status, headers, config) {
            controller.niches = data;
        }).error(function(data, status, headers, config) {
            console.log(data)
        });
        controller.getKeywords();
    };

    this.updateCategories = function() {
        $http.get("{{ settings.absurl("/api/categories") }}").success(function(data, status, headers, config) {
            controller.categories = data;
        }).error(function(data, status, headers, config) {
            console.log(data)
        });
        controller.getKeywords();
    };

    this.createCategory = (function(name){

        $http.post("{{ settings.absurl("/api/categories") }}", {name: name})
            .success(function(data, status, headers, config) {
                controller.categories = categories;
            })
            .error(function(data, status, headers, config) {
                console.log(data)
            });

        controller.updateCategories();
    });
    this.createNiche = (function(name){
        $http.post("{{ settings.absurl("/api/niches") }}", {name: name})
            .success(function(data, status, headers, config) {
                controller.niches = niches;
            })
            .error(function(data, status, headers, config) {
                console.log(data)
            });
        controller.updateNiches();
    });
    this.deleteNiche = (function(id){
        $http.delete("/api/niche/" + id, {name: name})
            .error(function(data, status, headers, config) {
                console.log(data)
            });
        controller.updateNiches();
    });
    this.deleteCategory = (function(id){
        $http.delete("/api/category/" + id, {name: name})
            .error(function(data, status, headers, config) {
                console.log(data)
            });
        controller.updateCategories();
    });
    this.getKeywords = function(){
        $http.get("/api/keywords")
            .success(function(data, status, headers, config) {
                controller.keywords = data;
            })
            .error(function(data, status, headers, config) {
                console.log(data)
            });
    };
    controller.updateNiches();
    controller.updateCategories();

    window.setTimeout(function(){
        controller.updateNiches();
        controller.updateCategories();
        controller.getKeywords();
    }, 1000);
});
