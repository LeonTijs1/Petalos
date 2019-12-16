var token = '1362124742.7b33a8d.6613a3567f0a425f9852055b8ef743b7',
    container2 = document.getElementById( 'rudr_userinfo' ),
    scrElement2 = document.createElement( 'script' );
 
window.mishaProcessResult2 = function( response ) {
	container2.innerHTML = '<div><p><img src="' + response.data.profile_picture + '"></p></div>'
		+ '<div><h1>' + response.data.username + '</h1>'
		+ '<p>#' + response.data.id + '</p>'
		+ '<p>' + response.data.counts.media + ' media ' + response.data.counts.followed_by + ' followers ' + response.data.counts.follows + ' follows</p>'
		+ '<p><strong>' + response.data.full_name + '</strong> ' + response.data.bio + '<a href="' + response.data.website + '">' + response.data.website + '</a></p></div>';
}
 
scrElement2.setAttribute( 'src', 'https://api.instagram.com/v1/users/self?access_token=' + token + '&callback=mishaProcessResult2' );
document.body.appendChild( scrElement2 );