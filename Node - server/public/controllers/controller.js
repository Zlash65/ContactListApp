var myApp = angular.module('myApp', []);

myApp.controller('AppCtrl', ['$scope', '$http', function($scope, $http){
	// console.log("Hello!!");

	var flag = 0;

	var refresh = function(){
		$http.get('/contactlist').success(function(response){
			// console.log("I got the data i requested");
			$scope.contactlist = response;
			$scope.contact = "";
		});
	};

	refresh();

	$scope.addContact = function(){
		if(flag == 1){
			// console.log(flag);
		}
		else{
			// console.log($scope.contact.name);
			$http.post('/contactlist', $scope.contact).success(function(response){
				// console.log("I got the data i requested");
				$scope.contactlist = response;
				refresh();
			});
			flag = 0;
		}
	};

	$scope.remove = function(id) {
		// console.log(id);
		$http.delete('/contactlist/' + id).success(function(response){
			refresh();
		});
	};

	$scope.edit = function(id) {
		flag = 1;
		// console.log(flag);
		// console.log(id);
		$http.get('/contactlist/' + id).success(function(response){
			$scope.contact = response;
		});
	};

	$scope.update = function(){
		// console.log(flag);
		$http.put('/contactlist/' + $scope.contact._id, $scope.contact).success(function(repsonse){
			refresh();
			// flag = 0;
		});
		flag = 0;
	};

}]);