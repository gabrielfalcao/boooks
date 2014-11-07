angular.module("BoooksApp.Auth", [
    "BoooksApp.Common",
]).controller('LoginController', function($rootScope, $scope, $state, $http, localStorageService){
    if ((typeof $rootScope.boooksAuthToken === 'string') && ($rootScope.boooksAuthToken.length > 0)) {
        $rootScope.boooksAuthToken = localStorageService.get("token");
        $state.go('index');
        return;
    }
    $scope.authenticate = function(){
        $rootScope.boooksAuthToken = $scope.token;
        localStorageService.add("token", $scope.token);
        $state.go('index');
    };
});
