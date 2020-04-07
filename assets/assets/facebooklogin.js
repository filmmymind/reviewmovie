        
  window.fbAsyncInit = function() {
    FB.init({
      appId      : '2959731660723879',
      cookie     : true,
      xfbml      : true,
      version    : 'v4.0'
    });
      

    FB.getLoginStatus(function(response) {
        statusChangeCallback(response);
    });
  };

  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "https://connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));

   function statusChangeCallback(response){
       if(response.status ==='connected'){
           console.log('login');
       }else{
           console.log('fail');
       }
   }

   
function checkLoginState() {
  FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
  });
}