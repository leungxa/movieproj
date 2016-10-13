angular.module('moviesApp', [])
.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
})
.controller('moviesController', function($scope, moviesService) {
  $scope.popularMovies = null;
  $scope.searchedQuery = null;
  $scope.queryResults = null;

  $scope.loadPopular = function() {
    moviesService.fetchPopularMovies()
      .success(function(data){
        $scope.popularMovies = []
        for (var i=0; i < 10; i++) {
          $scope.popularMovies.push(data.results[i]);
        }
      }).error(function(){
        alert('error fetching popular movies');
      });
  };

  $scope.loadPopular();

  $scope.searchQuery = function(query) {
    moviesService.searchMovies(query)
      .success(function(data){
        $scope.searchedQuery = data.query;
        $scope.queryResults = data.results;
      }).error(function(){
        alert('error searching for ' + query);
      });
  };

})
.service('moviesService', function($http) {
  this.fetchPopularMovies = function(query) {
    var targetURL = '/movies/popular/';
    return $http({
      method: 'GET',
      url: targetURL,
    });
  };

  this.searchMovies = function(query) {
    var targetURL = '/movies/search/?query=' + query;
    return $http({
      method: 'GET',
      url: targetURL,
    });
  };
});