angular.module("BoooksApp.Index", [
    "BoooksApp.Common",
]).controller('IndexController', function($rootScope, $scope, $state, $http){
    $rootScope.isAuthenticated();


});
